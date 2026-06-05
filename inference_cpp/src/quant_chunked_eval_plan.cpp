#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct Batch {
    std::string label;
    std::string config;
    std::string summary;
    std::string guard;
    bool existing = false;
};

struct Options {
    std::string model = "Qwen/Qwen3-1.7B";
    std::string prompts = "data_eval/text_prompts/c4_en_validation_128.txt";
    int limit_prompts = 128;
    int max_length = 128;
    std::string device = "cuda";
    std::string dtype = "float16";
    int group_size = 128;
    bool reuse_model = false;
    double max_memory_ratio = 0.85;
    double poll_seconds = 0.5;
    std::string dataset = "c4_128";
    std::string target = "wikitext_c4_consensus";
    std::string prefix = "random_budget_seed_";
    int seed_start = 20260604;
    int seed_end = 20260619;
    std::string merged_summary = "outputs/qwen3_1p7b_c4_128_consensus_random16_merged_ppl_summary.json";
    std::string evidence_md = "outputs/qwen3_1p7b_c4_128_consensus_random16_evidence_matrix.md";
    std::string audit_md = "outputs/qwen3_1p7b_c4_128_consensus_random16_random_seed_audit.md";
    std::string guard_md = "outputs/qwen3_1p7b_c4_128_consensus_random16_gpu_guard_summary.md";
    std::string emit = "bash";
    std::vector<Batch> batches;
};

std::string shell_quote(const std::string& value) {
    if (value.empty()) return "''";
    bool simple = true;
    for (const char ch : value) {
        const bool ok = std::isalnum(static_cast<unsigned char>(ch)) || ch == '_' || ch == '-' ||
                        ch == '/' || ch == '.' || ch == ':' || ch == '=' || ch == '+';
        if (!ok) {
            simple = false;
            break;
        }
    }
    if (simple) return value;
    std::string out = "'";
    for (const char ch : value) {
        if (ch == '\'') {
            out += "'\\''";
        } else {
            out.push_back(ch);
        }
    }
    out.push_back('\'');
    return out;
}

Batch parse_batch_arg(const std::string& text, bool existing) {
    std::vector<std::string> parts;
    std::size_t start = 0;
    while (start <= text.size()) {
        const std::size_t pos = text.find(':', start);
        if (pos == std::string::npos) {
            parts.push_back(text.substr(start));
            break;
        }
        parts.push_back(text.substr(start, pos - start));
        start = pos + 1;
    }
    if (parts.size() < 4) {
        throw std::runtime_error("batch format must be label:config:summary:guard");
    }
    Batch batch;
    batch.label = parts[0];
    batch.config = parts[1];
    batch.summary = parts[2];
    batch.guard = parts[3];
    batch.existing = existing;
    if (batch.label.empty() || batch.config.empty() || batch.summary.empty() || batch.guard.empty()) {
        throw std::runtime_error("batch fields must be non-empty");
    }
    return batch;
}

void add_default_batches(Options& options) {
    if (!options.batches.empty()) return;
    options.batches.push_back(Batch{
        "batch0",
        "data_eval/eval_configs/qwen3_1p7b_c4_128_consensus_random4_compare.json",
        "outputs/qwen3_1p7b_c4_128_consensus_random4_ppl_summary.json",
        "outputs/qwen3_1p7b_c4_128_consensus_random4_gpu_guard.json",
        true,
    });
    options.batches.push_back(Batch{
        "batch1",
        "data_eval/eval_configs/qwen3_1p7b_c4_128_random16_batch1_20260608_11.json",
        "outputs/qwen3_1p7b_c4_128_random16_batch1_ppl_summary.json",
        "outputs/qwen3_1p7b_c4_128_random16_batch1_gpu_guard.json",
        false,
    });
    options.batches.push_back(Batch{
        "batch2",
        "data_eval/eval_configs/qwen3_1p7b_c4_128_random16_batch2_20260612_15.json",
        "outputs/qwen3_1p7b_c4_128_random16_batch2_ppl_summary.json",
        "outputs/qwen3_1p7b_c4_128_random16_batch2_gpu_guard.json",
        false,
    });
    options.batches.push_back(Batch{
        "batch3",
        "data_eval/eval_configs/qwen3_1p7b_c4_128_random16_batch3_20260616_19.json",
        "outputs/qwen3_1p7b_c4_128_random16_batch3_ppl_summary.json",
        "outputs/qwen3_1p7b_c4_128_random16_batch3_gpu_guard.json",
        false,
    });
}

Options parse_args(int argc, char** argv) {
    Options options;
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        auto require_value = [&](const std::string& flag) -> std::string {
            if (i + 1 >= argc) {
                throw std::runtime_error("missing value for " + flag);
            }
            return argv[++i];
        };
        if (arg == "--model") {
            options.model = require_value("--model");
        } else if (arg == "--prompts") {
            options.prompts = require_value("--prompts");
        } else if (arg == "--limit-prompts") {
            options.limit_prompts = std::stoi(require_value("--limit-prompts"));
        } else if (arg == "--max-length") {
            options.max_length = std::stoi(require_value("--max-length"));
        } else if (arg == "--device") {
            options.device = require_value("--device");
        } else if (arg == "--dtype") {
            options.dtype = require_value("--dtype");
        } else if (arg == "--group-size") {
            options.group_size = std::stoi(require_value("--group-size"));
        } else if (arg == "--reuse-model") {
            options.reuse_model = true;
        } else if (arg == "--no-reuse-model") {
            options.reuse_model = false;
        } else if (arg == "--max-memory-ratio") {
            options.max_memory_ratio = std::stod(require_value("--max-memory-ratio"));
        } else if (arg == "--poll-seconds") {
            options.poll_seconds = std::stod(require_value("--poll-seconds"));
        } else if (arg == "--dataset") {
            options.dataset = require_value("--dataset");
        } else if (arg == "--target") {
            options.target = require_value("--target");
        } else if (arg == "--prefix") {
            options.prefix = require_value("--prefix");
        } else if (arg == "--seed-start") {
            options.seed_start = std::stoi(require_value("--seed-start"));
        } else if (arg == "--seed-end") {
            options.seed_end = std::stoi(require_value("--seed-end"));
        } else if (arg == "--merged-summary") {
            options.merged_summary = require_value("--merged-summary");
        } else if (arg == "--evidence-md") {
            options.evidence_md = require_value("--evidence-md");
        } else if (arg == "--audit-md") {
            options.audit_md = require_value("--audit-md");
        } else if (arg == "--guard-md") {
            options.guard_md = require_value("--guard-md");
        } else if (arg == "--batch") {
            options.batches.push_back(parse_batch_arg(require_value("--batch"), false));
        } else if (arg == "--existing-batch") {
            options.batches.push_back(parse_batch_arg(require_value("--existing-batch"), true));
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: quant_chunked_eval_plan [--emit bash|markdown]\n"
                      << "  [--reuse-model|--no-reuse-model]\n"
                      << "  [--existing-batch label:config:summary:guard] [--batch label:config:summary:guard]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    add_default_batches(options);
    if (options.emit != "bash" && options.emit != "markdown") {
        throw std::runtime_error("--emit must be bash or markdown");
    }
    if (options.seed_end < options.seed_start) {
        throw std::runtime_error("--seed-end must be >= --seed-start");
    }
    return options;
}

std::string coverage_command(const Options& options) {
    std::ostringstream cmd;
    cmd << "build/cpp-wsl/quant_seed_coverage_check";
    for (const Batch& batch : options.batches) {
        cmd << " \\\n  --input " << shell_quote(batch.config);
    }
    cmd << " \\\n  --prefix " << shell_quote(options.prefix)
        << " \\\n  --start " << options.seed_start
        << " \\\n  --end " << options.seed_end
        << " \\\n  --require-name fp16"
        << " \\\n  --require-name uniform_int4"
        << " \\\n  --require-name " << shell_quote(options.target)
        << " \\\n  --require-name cpp_category_budget"
        << " \\\n  --emit markdown";
    return cmd.str();
}

std::string eval_command(const Options& options, const Batch& batch) {
    std::ostringstream cmd;
    cmd << "python3 train_python/run_with_gpu_guard.py"
        << " --max-memory-ratio " << options.max_memory_ratio
        << " --poll-seconds " << options.poll_seconds
        << " --out " << shell_quote(batch.guard)
        << " -- \\\n  python3 train_python/eval_weight_quant_ppl.py"
        << " \\\n    --model " << shell_quote(options.model)
        << " \\\n    --prompts " << shell_quote(options.prompts)
        << " \\\n    --limit-prompts " << options.limit_prompts
        << " \\\n    --max-length " << options.max_length
        << " \\\n    --device " << shell_quote(options.device)
        << " \\\n    --dtype " << shell_quote(options.dtype)
        << " \\\n    --config-json " << shell_quote(batch.config)
        << " \\\n    --group-size " << options.group_size;
    if (options.reuse_model) {
        cmd << " \\\n    --reuse-model";
    }
    cmd << " \\\n    --out " << shell_quote(batch.summary);
    return cmd.str();
}

std::string merge_command(const Options& options) {
    std::ostringstream cmd;
    cmd << "build/cpp-wsl/quant_ppl_summary_merge";
    for (const Batch& batch : options.batches) {
        cmd << " \\\n  --input " << shell_quote(batch.summary);
    }
    cmd << " \\\n  --out " << shell_quote(options.merged_summary);
    return cmd.str();
}

std::string evidence_command(const Options& options) {
    std::ostringstream cmd;
    cmd << "build/cpp-wsl/quant_evidence_matrix"
        << " \\\n  --input " << shell_quote(options.merged_summary)
        << " \\\n  --dataset " << shell_quote(options.dataset)
        << " \\\n  --target " << shell_quote(options.target)
        << " \\\n  --emit markdown > " << shell_quote(options.evidence_md);
    return cmd.str();
}

std::string audit_command(const Options& options) {
    std::ostringstream cmd;
    cmd << "build/cpp-wsl/quant_random_baseline_audit"
        << " \\\n  --input " << shell_quote(options.merged_summary)
        << " \\\n  --dataset " << shell_quote(options.dataset)
        << " \\\n  --target " << shell_quote(options.target)
        << " \\\n  --emit markdown > " << shell_quote(options.audit_md);
    return cmd.str();
}

std::string guard_command(const Options& options) {
    std::ostringstream cmd;
    cmd << "build/cpp-wsl/gpu_guard_summary";
    for (const Batch& batch : options.batches) {
        cmd << " \\\n  --input " << shell_quote(batch.label + "=" + batch.guard);
    }
    cmd << " \\\n  --emit markdown > " << shell_quote(options.guard_md);
    return cmd.str();
}

void emit_bash(const Options& options) {
    std::cout << "#!/usr/bin/env bash\n";
    std::cout << "set -euo pipefail\n\n";
    if (!options.reuse_model) {
        std::cout << "# Low-memory mode: reload per config instead of caching all Linear weights.\n";
        std::cout << "# This is slower but avoids the 85% VRAM guard failure seen with --reuse-model.\n\n";
    }
    std::cout << "# Check planned random-seed coverage before spending GPU time.\n";
    std::cout << coverage_command(options) << "\n\n";
    for (const Batch& batch : options.batches) {
        if (batch.existing) {
            std::cout << "# Existing batch " << batch.label << ": " << batch.summary << "\n";
            continue;
        }
        std::cout << "# Run " << batch.label << "\n";
        std::cout << eval_command(options, batch) << "\n\n";
    }
    std::cout << "# Merge chunked summaries and regenerate evidence artifacts.\n";
    std::cout << merge_command(options) << "\n\n";
    std::cout << evidence_command(options) << "\n\n";
    std::cout << audit_command(options) << "\n\n";
    std::cout << guard_command(options) << "\n";
}

void emit_markdown(const Options& options) {
    std::cout << "# Chunked Quant Eval Plan\n\n";
    std::cout << "- model: `" << options.model << "`\n";
    std::cout << "- prompts: `" << options.prompts << "`\n";
    std::cout << "- target: `" << options.target << "`\n";
    std::cout << "- GPU guard: `" << options.max_memory_ratio << "`\n\n";
    std::cout << "- reuse model: `" << (options.reuse_model ? "true" : "false") << "`\n";
    if (!options.reuse_model) {
        std::cout << "- memory mode: low-memory, reload each config to avoid cached Linear-weight peaks\n";
    }
    std::cout << "\n";
    std::cout << "## Seed Coverage\n\n```bash\n" << coverage_command(options) << "\n```\n\n";
    std::cout << "## GPU Batches\n\n";
    for (const Batch& batch : options.batches) {
        std::cout << "### " << batch.label << "\n\n";
        if (batch.existing) {
            std::cout << "Existing summary: `" << batch.summary << "`\n\n";
        } else {
            std::cout << "```bash\n" << eval_command(options, batch) << "\n```\n\n";
        }
    }
    std::cout << "## Merge And Evidence\n\n";
    std::cout << "```bash\n" << merge_command(options) << "\n\n"
              << evidence_command(options) << "\n\n"
              << audit_command(options) << "\n\n"
              << guard_command(options) << "\n```\n";
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        if (options.emit == "bash") {
            emit_bash(options);
        } else {
            emit_markdown(options);
        }
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << "\n";
        return 1;
    }
}
