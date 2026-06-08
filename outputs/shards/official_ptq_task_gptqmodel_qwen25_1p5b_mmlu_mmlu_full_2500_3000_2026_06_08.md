# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 276 / 500 | 0.5520 | 8.9440 | 0.179622 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_2500` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2501` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2502` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2503` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2504` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2505` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2506` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2507` | `mcq` | false | `D` | `A. Sx` |
| baseline | `mmlu_2508` | `mcq` | true | `D` | `D. Iwkj` |
| baseline | `mmlu_2509` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2510` | `mcq` | false | `A` | `B. Invalid. Counterexample when C is true and D is false.` |
| baseline | `mmlu_2511` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2512` | `mcq` | true | `A` | `A. Some cookies have oatmeal. If something's not being a cookie entails that it doesn't have chocolate chips, then this ` |
| baseline | `mmlu_2513` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2514` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2515` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2516` | `mcq` | false | `A` | `B. Invalid. Counterexample when O is true and P is false.` |
| baseline | `mmlu_2517` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2518` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2519` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2520` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2521` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2522` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2523` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2524` | `mcq` | false | `A` | `B. Invalid. Counterexample when A is true and B and C are false` |
| baseline | `mmlu_2525` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2526` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2527` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2528` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2529` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2530` | `mcq` | false | `D` | `B. Invalid. Counterexample when Y and Z are true and Z is false.` |
| baseline | `mmlu_2531` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2532` | `mcq` | false | `A` | `C. Every house is bigger than some apartment.` |
| baseline | `mmlu_2533` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2534` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2535` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2536` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2537` | `mcq` | true | `C` | `C. ~Mmis` |
| baseline | `mmlu_2538` | `mcq` | false | `D` | `B. Invalid. Counterexample when S and U are true and T is false.` |
| baseline | `mmlu_2539` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2540` | `mcq` | false | `D` | `B. Invalid. Counterexample when L, N, O, Q, and R are true and M and P are false` |
| baseline | `mmlu_2541` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2542` | `mcq` | false | `C` | `B. Contradictory` |
| baseline | `mmlu_2543` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2544` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2545` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2546` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2547` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2548` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2549` | `mcq` | true | `D` | `D. Gba` |
| baseline | `mmlu_2550` | `mcq` | true | `A` | `A. ~(∀x)(Lx ⊃ Rx)` |
| baseline | `mmlu_2551` | `mcq` | false | `A` | `B. Invalid. Counterexample when I and H are true and J and K are false` |
| baseline | `mmlu_2552` | `mcq` | false | `D` | `B. Contradictory` |
| baseline | `mmlu_2553` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2554` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2555` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2556` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2557` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2558` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2559` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2560` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2561` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2562` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2563` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2564` | `mcq` | false | `D` | `B. Invalid. Counterexample when L and M are true and K and N are false` |
| baseline | `mmlu_2565` | `mcq` | false | `D` | `B. Invalid. Counterexample when H is true and I and G are false` |
| baseline | `mmlu_2566` | `mcq` | false | `A` | `B. Invalid. Counterexample when M is true and N is false.` |
| baseline | `mmlu_2567` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2568` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2569` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2570` | `mcq` | false | `B` | `A. About $300` |
| baseline | `mmlu_2571` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2572` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2573` | `mcq` | false | `C` | `B. by 10 fold` |
| baseline | `mmlu_2574` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2575` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2576` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2577` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2578` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2579` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2580` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2581` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2582` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2583` | `mcq` | true | `B` | `B. 56%` |
| baseline | `mmlu_2584` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2585` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2586` | `mcq` | true | `C` | `C. 82%` |
| baseline | `mmlu_2587` | `mcq` | false | `C` | `A. About $3k` |
| baseline | `mmlu_2588` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2589` | `mcq` | false | `A` | `C. 65%` |
| baseline | `mmlu_2590` | `mcq` | false | `A` | `C. 64%` |
| baseline | `mmlu_2591` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2592` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2593` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2594` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2595` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2596` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2597` | `mcq` | false | `D` | `C. 50%` |
| baseline | `mmlu_2598` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2599` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2600` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2601` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2602` | `mcq` | false | `C` | `B. by 8 fold` |
| baseline | `mmlu_2603` | `mcq` | true | `D` | `D. 19` |
| baseline | `mmlu_2604` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2605` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2606` | `mcq` | false | `B` | `C. 55%` |
| baseline | `mmlu_2607` | `mcq` | false | `D` | `B. by 8 fold` |
| baseline | `mmlu_2608` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2609` | `mcq` | true | `B` | `B. 86%` |
| baseline | `mmlu_2610` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2611` | `mcq` | false | `C` | `A. Brazil` |
| baseline | `mmlu_2612` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2613` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2614` | `mcq` | false | `C` | `B. 14 million` |
| baseline | `mmlu_2615` | `mcq` | false | `A` | `B. 46%` |
| baseline | `mmlu_2616` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2617` | `mcq` | true | `C` | `C. 36%` |
| baseline | `mmlu_2618` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2619` | `mcq` | false | `B` | `C. 6%` |
| baseline | `mmlu_2620` | `mcq` | true | `B` | `B. supported mainly by cross-section, not time-series studies` |
| baseline | `mmlu_2621` | `mcq` | false | `B` | `A. 12 years` |
| baseline | `mmlu_2622` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2623` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2624` | `mcq` | true | `B` | `B. 75%` |
| baseline | `mmlu_2625` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2626` | `mcq` | false | `D` | `B. 25%` |
| baseline | `mmlu_2627` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2628` | `mcq` | false | `B` | `D. 65.20%` |
| baseline | `mmlu_2629` | `mcq` | false | `C` | `B. 30 million` |
| baseline | `mmlu_2630` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2631` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2632` | `mcq` | false | `C` | `B. 58%` |
| baseline | `mmlu_2633` | `mcq` | false | `B` | `D. False, False` |
| baseline | `mmlu_2634` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2635` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2636` | `mcq` | true | `B` | `B. Canada` |
| baseline | `mmlu_2637` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2638` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2639` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2640` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2641` | `mcq` | false | `B` | `A. 1.5 children per woman` |
| baseline | `mmlu_2642` | `mcq` | false | `C` | `B. $1,000` |
| baseline | `mmlu_2643` | `mcq` | false | `C` | `D. 80%` |
| baseline | `mmlu_2644` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2645` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2646` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2647` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2648` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2649` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2650` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2651` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2652` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2653` | `mcq` | false | `A` | `D. False, False` |
| baseline | `mmlu_2654` | `mcq` | false | `B` | `C. -40%` |
| baseline | `mmlu_2655` | `mcq` | false | `C` | `B. 56%` |
| baseline | `mmlu_2656` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2657` | `mcq` | false | `C` | `A. $150,000` |
| baseline | `mmlu_2658` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2659` | `mcq` | false | `D` | `B. Russia` |
| baseline | `mmlu_2660` | `mcq` | true | `A` | `A. India, Congo` |
| baseline | `mmlu_2661` | `mcq` | true | `D` | `D. 86%` |
| baseline | `mmlu_2662` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2663` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2664` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2665` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2666` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2667` | `mcq` | true | `C` | `C. 80%` |
| baseline | `mmlu_2668` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2669` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2670` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2671` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2672` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2673` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2674` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2675` | `mcq` | true | `B` | `B. Phagocytes` |
| baseline | `mmlu_2676` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2677` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2678` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2679` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2680` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2681` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2682` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2683` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2684` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2685` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2686` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2687` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2688` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2689` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2690` | `mcq` | true | `C` | `C. mutualism` |
| baseline | `mmlu_2691` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2692` | `mcq` | true | `B` | `B. maintaining homeostasis.` |
| baseline | `mmlu_2693` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2694` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2695` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2696` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2697` | `mcq` | true | `C` | `C. Mutations` |
| baseline | `mmlu_2698` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2699` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2700` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2701` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2702` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2703` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2704` | `mcq` | true | `C` | `C. 54%` |
| baseline | `mmlu_2705` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2706` | `mcq` | true | `D` | `D. Mutations contribute the most to genetic variability in a population through natural mutations and other mutagens.` |
| baseline | `mmlu_2707` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2708` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2709` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2710` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2711` | `mcq` | false | `B` | `A. Some mosquitoes experienced a mutation after being exposed to DDT that made them resistant to the insecticide. Then t` |
| baseline | `mmlu_2712` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2713` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2714` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2715` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2716` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2717` | `mcq` | true | `B` | `B. fallopian tube` |
| baseline | `mmlu_2718` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2719` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2720` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2721` | `mcq` | true | `A` | `A. mitochondrial matrix` |
| baseline | `mmlu_2722` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2723` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2724` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2725` | `mcq` | false | `C` | `D. Promoter` |
| baseline | `mmlu_2726` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2727` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2728` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2729` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2730` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2731` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2732` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2733` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2734` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2735` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2736` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2737` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2738` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2739` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2740` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2741` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2742` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2743` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2744` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2745` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2746` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_2747` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2748` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2749` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2750` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2751` | `mcq` | true | `C` | `C. Availability of water.` |
| baseline | `mmlu_2752` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2753` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2754` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2755` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2756` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2757` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2758` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2759` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2760` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2761` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2762` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2763` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2764` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2765` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2766` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2767` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2768` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2769` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2770` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2771` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2772` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2773` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2774` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2775` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2776` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2777` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2778` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2779` | `mcq` | false | `C` | `B. Reproductive isolation was not complete.` |
| baseline | `mmlu_2780` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2781` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2782` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2783` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2784` | `mcq` | false | `B` | `D. 50%` |
| baseline | `mmlu_2785` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2786` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2787` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2788` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2789` | `mcq` | true | `A` | `A. enzymes in the lysosomes` |
| baseline | `mmlu_2790` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2791` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2792` | `mcq` | true | `D` | `D. 25%` |
| baseline | `mmlu_2793` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2794` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2795` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2796` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2797` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2798` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2799` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2800` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2801` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2802` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2803` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2804` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2805` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2806` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2807` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2808` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2809` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2810` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2811` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2812` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2813` | `mcq` | true | `A` | `A. Characteristics acquired during an organism's life are generally not passed on through genes.` |
| baseline | `mmlu_2814` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2815` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2816` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2817` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2818` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2819` | `mcq` | true | `B` | `B. The flu virus, which changes its envelope proteins` |
| baseline | `mmlu_2820` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2821` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2822` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2823` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2824` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2825` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2826` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2827` | `mcq` | true | `D` | `D. Promoter` |
| baseline | `mmlu_2828` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2829` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2830` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2831` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2832` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2833` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2834` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2835` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2836` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2837` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2838` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2839` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2840` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2841` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2842` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2843` | `mcq` | false | `D` | `A. Lake B is alkaline.` |
| baseline | `mmlu_2844` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2845` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2846` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2847` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2848` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2849` | `mcq` | true | `C` | `C.水` |
| baseline | `mmlu_2850` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2851` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2852` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2853` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2854` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2855` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2856` | `mcq` | true | `A` | `A. Enhancer` |
| baseline | `mmlu_2857` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2858` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2859` | `mcq` | false | `C` | `A. thicker walls, which are impermeable to water` |
| baseline | `mmlu_2860` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2861` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2862` | `mcq` | true | `D` | `D. I and III` |
| baseline | `mmlu_2863` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2864` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2865` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2866` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2867` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2868` | `mcq` | true | `A` | `A. increasing the surface area of the small intestine.` |
| baseline | `mmlu_2869` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2870` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2871` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2872` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2873` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2874` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2875` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2876` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2877` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2878` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2879` | `mcq` | true | `B` | `B. Differences in the timing and expression levels of different genes leads to structural and functional differences.` |
| baseline | `mmlu_2880` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2881` | `mcq` | true | `C` | `C. The frequency of the allele will remain at 0.3 because the population is at Hardy-Weinberg equilibrium.` |
| baseline | `mmlu_2882` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2883` | `mcq` | true | `B` | `B. Minimizing artificial lighting in the area` |
| baseline | `mmlu_2884` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2885` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2886` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2887` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2888` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2889` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2890` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2891` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2892` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2893` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2894` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2895` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2896` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2897` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2898` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2899` | `mcq` | true | `B` | `B. Repressor` |
| baseline | `mmlu_2900` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2901` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2902` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2903` | `mcq` | false | `B` | `A. removing some of reactant A` |
| baseline | `mmlu_2904` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2905` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2906` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2907` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2908` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2909` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2910` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2911` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2912` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2913` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2914` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2915` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2916` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2917` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2918` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2919` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2920` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2921` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2922` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2923` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2924` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2925` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2926` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2927` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2928` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2929` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2930` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2931` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2932` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2933` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2934` | `mcq` | true | `B` | `B. Succession` |
| baseline | `mmlu_2935` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2936` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2937` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2938` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2939` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2940` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2941` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2942` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2943` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2944` | `mcq` | true | `A` | `A. H2O` |
| baseline | `mmlu_2945` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2946` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2947` | `mcq` | true | `A` | `A. Prophase I` |
| baseline | `mmlu_2948` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2949` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2950` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2951` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2952` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2953` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2954` | `mcq` | true | `D` | `D. Fungus` |
| baseline | `mmlu_2955` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2956` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2957` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2958` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2959` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2960` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2961` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2962` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2963` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2964` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2965` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2966` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2967` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2968` | `mcq` | true | `D` | `D. Natural selection` |
| baseline | `mmlu_2969` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2970` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2971` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2972` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2973` | `mcq` | false | `B` | `C. Adenine : Guanine` |
| baseline | `mmlu_2974` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2975` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2976` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2977` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2978` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2979` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2980` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2981` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2982` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2983` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2984` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2985` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2986` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2987` | `mcq` | false | `C` | `B. Se2-` |
| baseline | `mmlu_2988` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2989` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2990` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2991` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2992` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2993` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2994` | `mcq` | false | `C` | `B. a weak acid` |
| baseline | `mmlu_2995` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2996` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2997` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2998` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2999` | `mcq` | false | `B` | `C.` |
