# ESMP Activation Reconstruction Report

Date: `2026-06-06`
Model: `Qwen/Qwen3-0.6B`
Package summary: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/qwen3_0p6b_full_esmp/pack_summary.json`
Prompts: `4`
Max length: `96`
Sample rows per module: `32`
Device: `cuda`

## Aggregate

- Modules OK: `196/196`
- Median output rel-L2: `0.136343`
- P90 output rel-L2: `0.211388`
- Median normalized output MSE: `0.01858965`
- Median weight rel-L2: `0.157550`
- Median compression vs FP32: `7.6414x`
- Peak CUDA memory allocated by script: `1193.70 MiB`

## Family Summary

| family | modules | median output rel-L2 | median compression vs FP32 |
|---|---:|---:|---:|
| attention | 112 | 0.135070 | 7.6409x |
| mlp | 84 | 0.160471 | 7.6415x |

## Per-Module Results (196)

| module | bits | sample rows | output rel-L2 | norm MSE | weight rel-L2 | compression |
|---|---:|---:|---:|---:|---:|---:|
| `model.layers.20.self_attn.v_proj` | 4 | 32 | 0.281068 | 0.07899929 | 0.189248 | 7.6409x |
| `model.layers.13.self_attn.o_proj` | 4 | 32 | 0.272646 | 0.07433590 | 0.173153 | 7.8163x |
| `model.layers.23.self_attn.v_proj` | 4 | 32 | 0.261149 | 0.06819893 | 0.181827 | 7.6409x |
| `model.layers.9.self_attn.o_proj` | 4 | 32 | 0.257773 | 0.06644713 | 0.196486 | 7.8163x |
| `model.layers.22.self_attn.v_proj` | 4 | 32 | 0.253620 | 0.06432286 | 0.176034 | 7.6409x |
| `model.layers.21.self_attn.v_proj` | 4 | 32 | 0.247250 | 0.06113275 | 0.172914 | 7.6409x |
| `model.layers.24.self_attn.v_proj` | 4 | 32 | 0.241830 | 0.05848165 | 0.171804 | 7.6409x |
| `model.layers.11.self_attn.o_proj` | 4 | 32 | 0.241483 | 0.05831406 | 0.209147 | 7.8163x |
| `model.layers.17.self_attn.o_proj` | 4 | 32 | 0.237780 | 0.05653941 | 0.184291 | 7.8163x |
| `model.layers.19.mlp.down_proj` | 4 | 32 | 0.233969 | 0.05474127 | 0.215156 | 7.8766x |
| `model.layers.14.mlp.down_proj` | 4 | 32 | 0.233715 | 0.05462271 | 0.201329 | 7.8766x |
| `model.layers.18.mlp.down_proj` | 4 | 32 | 0.228433 | 0.05218144 | 0.205428 | 7.8766x |
| `model.layers.12.self_attn.o_proj` | 4 | 32 | 0.222140 | 0.04934633 | 0.167559 | 7.8163x |
| `model.layers.25.self_attn.v_proj` | 4 | 32 | 0.221402 | 0.04901868 | 0.168323 | 7.6409x |
| `model.layers.13.mlp.down_proj` | 4 | 32 | 0.220677 | 0.04869816 | 0.196800 | 7.8766x |
| `model.layers.15.mlp.down_proj` | 4 | 32 | 0.219622 | 0.04823401 | 0.197314 | 7.8766x |
| `model.layers.12.mlp.down_proj` | 4 | 32 | 0.216910 | 0.04705016 | 0.189331 | 7.8766x |
| `model.layers.11.mlp.down_proj` | 4 | 32 | 0.216598 | 0.04691453 | 0.192386 | 7.8766x |
| `model.layers.10.mlp.down_proj` | 4 | 32 | 0.213754 | 0.04569079 | 0.204218 | 7.8766x |
| `model.layers.17.mlp.down_proj` | 4 | 32 | 0.212168 | 0.04501523 | 0.196879 | 7.8766x |
| `model.layers.26.self_attn.v_proj` | 4 | 32 | 0.210608 | 0.04435587 | 0.157183 | 7.6409x |
| `model.layers.1.mlp.up_proj` | 4 | 32 | 0.208204 | 0.04334895 | 0.152634 | 7.6415x |
| `model.layers.4.self_attn.o_proj` | 4 | 32 | 0.205979 | 0.04242724 | 0.182920 | 7.8163x |
| `model.layers.10.self_attn.o_proj` | 4 | 32 | 0.205005 | 0.04202687 | 0.176292 | 7.8163x |
| `model.layers.21.mlp.down_proj` | 4 | 32 | 0.204917 | 0.04199092 | 0.197345 | 7.8766x |
| `model.layers.16.self_attn.o_proj` | 4 | 32 | 0.204558 | 0.04184401 | 0.180449 | 7.8163x |
| `model.layers.20.mlp.down_proj` | 4 | 32 | 0.204049 | 0.04163582 | 0.201509 | 7.8766x |
| `model.layers.9.mlp.down_proj` | 4 | 32 | 0.201135 | 0.04045532 | 0.187377 | 7.8766x |
| `model.layers.15.self_attn.o_proj` | 4 | 32 | 0.201032 | 0.04041392 | 0.177382 | 7.8163x |
| `model.layers.3.mlp.up_proj` | 4 | 32 | 0.198056 | 0.03922610 | 0.153068 | 7.6415x |
| `model.layers.7.mlp.down_proj` | 4 | 32 | 0.195408 | 0.03818416 | 0.191008 | 7.8766x |
| `model.layers.12.mlp.up_proj` | 4 | 32 | 0.194214 | 0.03771926 | 0.155419 | 7.6415x |
| `model.layers.9.self_attn.v_proj` | 4 | 32 | 0.194047 | 0.03765426 | 0.162738 | 7.6409x |
| `model.layers.7.self_attn.v_proj` | 4 | 32 | 0.194028 | 0.03764705 | 0.159974 | 7.6409x |
| `model.layers.4.mlp.down_proj` | 4 | 32 | 0.191951 | 0.03684509 | 0.185914 | 7.8766x |
| `model.layers.3.self_attn.v_proj` | 4 | 32 | 0.189362 | 0.03585782 | 0.159015 | 7.6409x |
| `model.layers.13.mlp.up_proj` | 4 | 32 | 0.189154 | 0.03577924 | 0.155792 | 7.6415x |
| `model.layers.23.mlp.down_proj` | 4 | 32 | 0.188834 | 0.03565816 | 0.188411 | 7.8766x |
| `model.layers.27.mlp.up_proj` | 4 | 32 | 0.188475 | 0.03552283 | 0.155976 | 7.6415x |
| `model.layers.5.self_attn.o_proj` | 4 | 32 | 0.187497 | 0.03515513 | 0.192686 | 7.8163x |
| `model.layers.8.self_attn.o_proj` | 4 | 32 | 0.186831 | 0.03490580 | 0.172282 | 7.8163x |
| `model.layers.8.mlp.down_proj` | 4 | 32 | 0.186570 | 0.03480841 | 0.182242 | 7.8766x |
| `model.layers.10.self_attn.v_proj` | 4 | 32 | 0.185995 | 0.03459402 | 0.151914 | 7.6409x |
| `model.layers.22.mlp.down_proj` | 4 | 32 | 0.184711 | 0.03411804 | 0.189232 | 7.8766x |
| `model.layers.4.self_attn.v_proj` | 4 | 32 | 0.184486 | 0.03403506 | 0.152366 | 7.6409x |
| `model.layers.5.mlp.down_proj` | 4 | 32 | 0.184266 | 0.03395388 | 0.184642 | 7.8766x |
| `model.layers.7.self_attn.o_proj` | 4 | 32 | 0.184233 | 0.03394169 | 0.168773 | 7.8163x |
| `model.layers.25.mlp.down_proj` | 4 | 32 | 0.183974 | 0.03384644 | 0.174906 | 7.8766x |
| `model.layers.23.self_attn.o_proj` | 4 | 32 | 0.183435 | 0.03364849 | 0.172648 | 7.8163x |
| `model.layers.3.mlp.down_proj` | 4 | 32 | 0.183030 | 0.03350000 | 0.181558 | 7.8766x |
| `model.layers.6.mlp.down_proj` | 4 | 32 | 0.182662 | 0.03336551 | 0.183101 | 7.8766x |
| `model.layers.26.self_attn.o_proj` | 4 | 32 | 0.182556 | 0.03332660 | 0.181405 | 7.8163x |
| `model.layers.11.mlp.up_proj` | 4 | 32 | 0.181783 | 0.03304503 | 0.153835 | 7.6415x |
| `model.layers.19.self_attn.o_proj` | 4 | 32 | 0.180850 | 0.03270687 | 0.184790 | 7.8163x |
| `model.layers.15.mlp.up_proj` | 4 | 32 | 0.180690 | 0.03264898 | 0.159892 | 7.6415x |
| `model.layers.21.self_attn.o_proj` | 4 | 32 | 0.179937 | 0.03237739 | 0.193736 | 7.8163x |
| `model.layers.16.mlp.up_proj` | 4 | 32 | 0.179268 | 0.03213691 | 0.167372 | 7.6415x |
| `model.layers.14.mlp.up_proj` | 4 | 32 | 0.178768 | 0.03195789 | 0.158326 | 7.6415x |
| `model.layers.23.mlp.up_proj` | 4 | 32 | 0.178081 | 0.03171281 | 0.153555 | 7.6415x |
| `model.layers.10.mlp.up_proj` | 4 | 32 | 0.177742 | 0.03159233 | 0.160020 | 7.6415x |
| `model.layers.24.mlp.down_proj` | 4 | 32 | 0.177602 | 0.03154254 | 0.181682 | 7.8766x |
| `model.layers.4.mlp.up_proj` | 4 | 32 | 0.177226 | 0.03140904 | 0.151632 | 7.6415x |
| `model.layers.25.mlp.up_proj` | 4 | 32 | 0.177134 | 0.03137644 | 0.152071 | 7.6415x |
| `model.layers.6.self_attn.o_proj` | 4 | 32 | 0.176641 | 0.03120220 | 0.176889 | 7.8163x |
| `model.layers.22.self_attn.o_proj` | 4 | 32 | 0.176600 | 0.03118760 | 0.171531 | 7.8163x |
| `model.layers.9.mlp.up_proj` | 4 | 32 | 0.175374 | 0.03075600 | 0.151844 | 7.6415x |
| `model.layers.22.mlp.up_proj` | 4 | 32 | 0.175135 | 0.03067214 | 0.156349 | 7.6415x |
| `model.layers.20.self_attn.o_proj` | 4 | 32 | 0.173475 | 0.03009369 | 0.183830 | 7.8163x |
| `model.layers.5.mlp.up_proj` | 4 | 32 | 0.172519 | 0.02976264 | 0.152773 | 7.6415x |
| `model.layers.21.self_attn.k_proj` | 4 | 32 | 0.172251 | 0.02967046 | 0.177065 | 7.6409x |
| `model.layers.6.mlp.up_proj` | 4 | 32 | 0.171770 | 0.02950476 | 0.151407 | 7.6415x |
| `model.layers.27.self_attn.o_proj` | 4 | 32 | 0.170521 | 0.02907750 | 0.158777 | 7.8163x |
| `model.layers.7.mlp.up_proj` | 4 | 32 | 0.168993 | 0.02855855 | 0.150891 | 7.6415x |
| `model.layers.18.self_attn.o_proj` | 4 | 32 | 0.168493 | 0.02838975 | 0.173466 | 7.8163x |
| `model.layers.21.mlp.up_proj` | 4 | 32 | 0.167296 | 0.02798797 | 0.159426 | 7.6415x |
| `model.layers.14.self_attn.o_proj` | 4 | 32 | 0.163775 | 0.02682210 | 0.167788 | 7.8163x |
| `model.layers.3.self_attn.o_proj` | 4 | 32 | 0.163396 | 0.02669829 | 0.178078 | 7.8163x |
| `model.layers.1.self_attn.v_proj` | 4 | 32 | 0.163377 | 0.02669209 | 0.150430 | 7.6409x |
| `model.layers.19.mlp.up_proj` | 4 | 32 | 0.160526 | 0.02576848 | 0.168187 | 7.6415x |
| `model.layers.0.mlp.up_proj` | 4 | 32 | 0.160416 | 0.02573345 | 0.152933 | 7.6415x |
| `model.layers.16.self_attn.k_proj` | 4 | 32 | 0.157525 | 0.02481399 | 0.181479 | 7.6409x |
| `model.layers.20.mlp.up_proj` | 4 | 32 | 0.157095 | 0.02467880 | 0.160515 | 7.6415x |
| `model.layers.22.self_attn.q_proj` | 4 | 32 | 0.156835 | 0.02459719 | 0.154904 | 7.6413x |
| `model.layers.21.self_attn.q_proj` | 4 | 32 | 0.155492 | 0.02417773 | 0.155223 | 7.6413x |
| `model.layers.18.self_attn.k_proj` | 4 | 32 | 0.152459 | 0.02324372 | 0.167277 | 7.6409x |
| `model.layers.1.self_attn.o_proj` | 4 | 32 | 0.151249 | 0.02287641 | 0.167981 | 7.8163x |
| `model.layers.25.self_attn.o_proj` | 4 | 32 | 0.149822 | 0.02244665 | 0.164958 | 7.8163x |
| `model.layers.26.self_attn.k_proj` | 4 | 32 | 0.146323 | 0.02141037 | 0.170778 | 7.6409x |
| `model.layers.0.self_attn.o_proj` | 4 | 32 | 0.145276 | 0.02110525 | 0.189837 | 7.8163x |
| `model.layers.19.self_attn.k_proj` | 4 | 32 | 0.144857 | 0.02098369 | 0.166620 | 7.6409x |
| `model.layers.19.self_attn.q_proj` | 4 | 32 | 0.143438 | 0.02057436 | 0.154459 | 7.6413x |
| `model.layers.24.self_attn.k_proj` | 4 | 32 | 0.143437 | 0.02057407 | 0.176665 | 7.6409x |
| `model.layers.17.self_attn.k_proj` | 4 | 32 | 0.139076 | 0.01934215 | 0.169791 | 7.6409x |
| `model.layers.14.self_attn.q_proj` | 4 | 32 | 0.138689 | 0.01923477 | 0.157917 | 7.6413x |
| `model.layers.24.self_attn.q_proj` | 4 | 32 | 0.137877 | 0.01901019 | 0.163756 | 7.6413x |
| `model.layers.17.mlp.gate_proj` | 4 | 32 | 0.137588 | 0.01893039 | 0.170363 | 7.6415x |
| `model.layers.26.mlp.gate_proj` | 4 | 32 | 0.137077 | 0.01879004 | 0.163461 | 7.6415x |
| `model.layers.15.self_attn.q_proj` | 4 | 32 | 0.136673 | 0.01867947 | 0.154891 | 7.6413x |
| `model.layers.2.self_attn.o_proj` | 4 | 32 | 0.136014 | 0.01849982 | 0.179010 | 7.8163x |
| `model.layers.17.self_attn.q_proj` | 4 | 32 | 0.135765 | 0.01843216 | 0.159323 | 7.6413x |
| `model.layers.3.self_attn.k_proj` | 4 | 32 | 0.135664 | 0.01840464 | 0.170262 | 7.6409x |
| `model.layers.25.self_attn.q_proj` | 4 | 32 | 0.135085 | 0.01824784 | 0.162490 | 7.6413x |
| `model.layers.18.self_attn.q_proj` | 4 | 32 | 0.135056 | 0.01824020 | 0.154565 | 7.6413x |
| `model.layers.16.self_attn.q_proj` | 4 | 32 | 0.133580 | 0.01784368 | 0.155002 | 7.6413x |
| `model.layers.18.mlp.gate_proj` | 4 | 32 | 0.133444 | 0.01780743 | 0.174719 | 7.6415x |
| `model.layers.8.self_attn.v_proj` | 4 | 32 | 0.133134 | 0.01772463 | 0.152819 | 7.6409x |
| `model.layers.15.mlp.gate_proj` | 4 | 32 | 0.133110 | 0.01771823 | 0.165268 | 7.6415x |
| `model.layers.5.self_attn.q_proj` | 4 | 32 | 0.133061 | 0.01770511 | 0.154106 | 7.6413x |
| `model.layers.24.self_attn.o_proj` | 4 | 32 | 0.132216 | 0.01748113 | 0.160458 | 7.8163x |
| `model.layers.10.self_attn.q_proj` | 4 | 32 | 0.130859 | 0.01712417 | 0.155265 | 7.6413x |
| `model.layers.14.mlp.gate_proj` | 4 | 32 | 0.130615 | 0.01706041 | 0.161317 | 7.6415x |
| `model.layers.5.self_attn.k_proj` | 4 | 32 | 0.129927 | 0.01688092 | 0.154172 | 7.6409x |
| `model.layers.20.mlp.gate_proj` | 4 | 32 | 0.129517 | 0.01677456 | 0.169780 | 7.6415x |
| `model.layers.6.self_attn.k_proj` | 4 | 32 | 0.127600 | 0.01628169 | 0.166974 | 7.6409x |
| `model.layers.13.mlp.gate_proj` | 4 | 32 | 0.127092 | 0.01615229 | 0.158504 | 7.6415x |
| `model.layers.19.mlp.gate_proj` | 4 | 32 | 0.126961 | 0.01611921 | 0.174995 | 7.6415x |
| `model.layers.13.self_attn.q_proj` | 4 | 32 | 0.126612 | 0.01603054 | 0.152416 | 7.6413x |
| `model.layers.21.mlp.gate_proj` | 4 | 32 | 0.123845 | 0.01533749 | 0.166048 | 7.6415x |
| `model.layers.16.mlp.gate_proj` | 4 | 32 | 0.123628 | 0.01528387 | 0.166519 | 7.6415x |
| `model.layers.10.mlp.gate_proj` | 4 | 32 | 0.123614 | 0.01528044 | 0.156498 | 7.6415x |
| `model.layers.11.self_attn.k_proj` | 4 | 32 | 0.123463 | 0.01524300 | 0.166748 | 7.6409x |
| `model.layers.11.mlp.gate_proj` | 4 | 32 | 0.122665 | 0.01504670 | 0.155257 | 7.6415x |
| `model.layers.7.self_attn.q_proj` | 4 | 32 | 0.122558 | 0.01502052 | 0.154523 | 7.6413x |
| `model.layers.12.self_attn.q_proj` | 4 | 32 | 0.122056 | 0.01489769 | 0.152181 | 7.6413x |
| `model.layers.10.self_attn.k_proj` | 4 | 32 | 0.121828 | 0.01484204 | 0.151567 | 7.6409x |
| `model.layers.25.mlp.gate_proj` | 4 | 32 | 0.121531 | 0.01476983 | 0.156897 | 7.6415x |
| `model.layers.12.mlp.gate_proj` | 4 | 32 | 0.121204 | 0.01469051 | 0.154150 | 7.6415x |
| `model.layers.27.mlp.gate_proj` | 4 | 32 | 0.120107 | 0.01442569 | 0.161848 | 7.6415x |
| `model.layers.1.self_attn.q_proj` | 4 | 32 | 0.118496 | 0.01404122 | 0.156059 | 7.6413x |
| `model.layers.7.self_attn.k_proj` | 4 | 32 | 0.118310 | 0.01399728 | 0.155225 | 7.6409x |
| `model.layers.8.self_attn.q_proj` | 4 | 32 | 0.118264 | 0.01398631 | 0.156659 | 7.6413x |
| `model.layers.22.mlp.gate_proj` | 4 | 32 | 0.117420 | 0.01378737 | 0.162597 | 7.6415x |
| `model.layers.4.self_attn.q_proj` | 4 | 32 | 0.116039 | 0.01346508 | 0.154021 | 7.6413x |
| `model.layers.9.self_attn.q_proj` | 4 | 32 | 0.114351 | 0.01307624 | 0.157096 | 7.6413x |
| `model.layers.2.self_attn.q_proj` | 4 | 32 | 0.114170 | 0.01303478 | 0.158819 | 7.6413x |
| `model.layers.9.mlp.gate_proj` | 4 | 32 | 0.112388 | 0.01263099 | 0.151776 | 7.6415x |
| `model.layers.24.mlp.gate_proj` | 4 | 32 | 0.112386 | 0.01263053 | 0.156289 | 7.6415x |
| `model.layers.23.mlp.gate_proj` | 4 | 32 | 0.111363 | 0.01240176 | 0.155637 | 7.6415x |
| `model.layers.27.self_attn.q_proj` | 4 | 32 | 0.110455 | 0.01220036 | 0.150758 | 7.6413x |
| `model.layers.13.self_attn.v_proj` | 4 | 32 | 0.109940 | 0.01208685 | 0.151381 | 7.6409x |
| `model.layers.11.self_attn.q_proj` | 4 | 32 | 0.109684 | 0.01203066 | 0.158323 | 7.6413x |
| `model.layers.8.mlp.gate_proj` | 4 | 32 | 0.106369 | 0.01131444 | 0.149822 | 7.6415x |
| `model.layers.6.self_attn.q_proj` | 4 | 32 | 0.104696 | 0.01096123 | 0.156742 | 7.6413x |
| `model.layers.5.mlp.gate_proj` | 4 | 32 | 0.103575 | 0.01072779 | 0.149676 | 7.6415x |
| `model.layers.27.self_attn.k_proj` | 4 | 32 | 0.099345 | 0.00986943 | 0.156762 | 7.6409x |
| `model.layers.7.mlp.gate_proj` | 4 | 32 | 0.099104 | 0.00982163 | 0.148005 | 7.6415x |
| `model.layers.6.mlp.gate_proj` | 4 | 32 | 0.095550 | 0.00912982 | 0.149219 | 7.6415x |
| `model.layers.0.self_attn.q_proj` | 4 | 32 | 0.095515 | 0.00912312 | 0.166855 | 7.6413x |
| `model.layers.8.self_attn.k_proj` | 4 | 32 | 0.095440 | 0.00910875 | 0.178581 | 7.6409x |
| `model.layers.0.mlp.gate_proj` | 4 | 32 | 0.095332 | 0.00908810 | 0.152086 | 7.6415x |
| `model.layers.2.self_attn.k_proj` | 4 | 32 | 0.095000 | 0.00902503 | 0.155747 | 7.6409x |
| `model.layers.14.self_attn.k_proj` | 4 | 32 | 0.094325 | 0.00889723 | 0.168285 | 7.6409x |
| `model.layers.3.mlp.gate_proj` | 4 | 32 | 0.090046 | 0.00810822 | 0.149486 | 7.6415x |
| `model.layers.1.self_attn.k_proj` | 4 | 32 | 0.089242 | 0.00796418 | 0.154405 | 7.6409x |
| `model.layers.13.self_attn.k_proj` | 4 | 32 | 0.087998 | 0.00774359 | 0.161807 | 7.6409x |
| `model.layers.4.mlp.gate_proj` | 4 | 32 | 0.083849 | 0.00703064 | 0.147827 | 7.6415x |
| `model.layers.0.self_attn.k_proj` | 4 | 32 | 0.076153 | 0.00579932 | 0.150826 | 7.6409x |
| `model.layers.19.self_attn.v_proj` | 8 | 32 | 0.018109 | 0.00032794 | 0.009811 | 3.9082x |
| `model.layers.26.mlp.down_proj` | 8 | 32 | 0.017002 | 0.00028908 | 0.010086 | 3.9689x |
| `model.layers.18.self_attn.v_proj` | 8 | 32 | 0.016868 | 0.00028453 | 0.009105 | 3.9082x |
| `model.layers.17.self_attn.v_proj` | 8 | 32 | 0.016150 | 0.00026081 | 0.008826 | 3.9082x |
| `model.layers.15.self_attn.v_proj` | 8 | 32 | 0.015459 | 0.00023899 | 0.009095 | 3.9082x |
| `model.layers.16.self_attn.v_proj` | 8 | 32 | 0.014738 | 0.00021721 | 0.008771 | 3.9082x |
| `model.layers.27.self_attn.v_proj` | 8 | 32 | 0.014611 | 0.00021347 | 0.008388 | 3.9082x |
| `model.layers.16.mlp.down_proj` | 8 | 32 | 0.012345 | 0.00015241 | 0.012017 | 3.9689x |
| `model.layers.5.self_attn.v_proj` | 8 | 32 | 0.011818 | 0.00013966 | 0.008953 | 3.9082x |
| `model.layers.11.self_attn.v_proj` | 8 | 32 | 0.011716 | 0.00013726 | 0.009116 | 3.9082x |
| `model.layers.6.self_attn.v_proj` | 8 | 32 | 0.011362 | 0.00012909 | 0.008455 | 3.9082x |
| `model.layers.2.self_attn.v_proj` | 8 | 32 | 0.009881 | 0.00009763 | 0.008329 | 3.9082x |
| `model.layers.24.mlp.up_proj` | 8 | 32 | 0.009839 | 0.00009680 | 0.008335 | 3.9083x |
| `model.layers.17.mlp.up_proj` | 8 | 32 | 0.009720 | 0.00009448 | 0.008859 | 3.9083x |
| `model.layers.0.self_attn.v_proj` | 8 | 32 | 0.009684 | 0.00009377 | 0.008363 | 3.9082x |
| `model.layers.20.self_attn.k_proj` | 8 | 32 | 0.009558 | 0.00009135 | 0.009717 | 3.9082x |
| `model.layers.26.self_attn.q_proj` | 8 | 32 | 0.009529 | 0.00009081 | 0.008804 | 3.9083x |
| `model.layers.26.mlp.up_proj` | 8 | 32 | 0.009482 | 0.00008991 | 0.008470 | 3.9083x |
| `model.layers.8.mlp.up_proj` | 8 | 32 | 0.009463 | 0.00008954 | 0.008372 | 3.9083x |
| `model.layers.2.mlp.up_proj` | 8 | 32 | 0.009304 | 0.00008656 | 0.008539 | 3.9083x |
| `model.layers.23.self_attn.k_proj` | 8 | 32 | 0.009184 | 0.00008435 | 0.010068 | 3.9082x |
| `model.layers.1.mlp.down_proj` | 8 | 32 | 0.009155 | 0.00008381 | 0.010328 | 3.9689x |
| `model.layers.22.self_attn.k_proj` | 8 | 32 | 0.008982 | 0.00008068 | 0.009069 | 3.9082x |
| `model.layers.18.mlp.up_proj` | 8 | 32 | 0.008864 | 0.00007857 | 0.008951 | 3.9083x |
| `model.layers.0.mlp.down_proj` | 8 | 32 | 0.008673 | 0.00007523 | 0.009731 | 3.9689x |
| `model.layers.20.self_attn.q_proj` | 8 | 32 | 0.008428 | 0.00007103 | 0.008973 | 3.9083x |
| `model.layers.9.self_attn.k_proj` | 8 | 32 | 0.008073 | 0.00006518 | 0.009568 | 3.9082x |
| `model.layers.23.self_attn.q_proj` | 8 | 32 | 0.007974 | 0.00006359 | 0.008920 | 3.9083x |
| `model.layers.15.self_attn.k_proj` | 8 | 32 | 0.007762 | 0.00006025 | 0.008873 | 3.9082x |
| `model.layers.25.self_attn.k_proj` | 8 | 32 | 0.007608 | 0.00005789 | 0.009535 | 3.9082x |
| `model.layers.14.self_attn.v_proj` | 8 | 32 | 0.007244 | 0.00005248 | 0.008411 | 3.9082x |
| `model.layers.4.self_attn.k_proj` | 8 | 32 | 0.006671 | 0.00004451 | 0.008934 | 3.9082x |
| `model.layers.2.mlp.down_proj` | 8 | 32 | 0.006360 | 0.00004045 | 0.010908 | 3.9689x |
| `model.layers.12.self_attn.v_proj` | 8 | 32 | 0.006116 | 0.00003741 | 0.008357 | 3.9082x |
| `model.layers.3.self_attn.q_proj` | 8 | 32 | 0.005998 | 0.00003598 | 0.008772 | 3.9083x |
| `model.layers.27.mlp.down_proj` | 8 | 32 | 0.005663 | 0.00003207 | 0.011026 | 3.9689x |
| `model.layers.2.mlp.gate_proj` | 8 | 32 | 0.005224 | 0.00002729 | 0.008317 | 3.9083x |
| `model.layers.12.self_attn.k_proj` | 8 | 32 | 0.004351 | 0.00001893 | 0.008952 | 3.9082x |
| `model.layers.1.mlp.gate_proj` | 8 | 32 | 0.004275 | 0.00001828 | 0.008160 | 3.9083x |

## Scope

- This evaluates ESMP package reconstruction on sampled real module activations.
- It is a local module-quality check, not an end-to-end packed LLM runtime.
- The next step is replacing the selected Linear modules during generation and measuring TTFT/tokens/s.
