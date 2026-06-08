# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 296 / 500 | 0.5920 | 8.6359 | 0.191577 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_3000` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3001` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3002` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3003` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3004` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3005` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3006` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3007` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3008` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3009` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3010` | `mcq` | false | `D` | `B. -3` |
| baseline | `mmlu_3011` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3012` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3013` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3014` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3015` | `mcq` | false | `B` | `D. SF6` |
| baseline | `mmlu_3016` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3017` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3018` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3019` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3020` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3021` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3022` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3023` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3024` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3025` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3026` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3027` | `mcq` | true | `C` | `C. RCOOH` |
| baseline | `mmlu_3028` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3029` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3030` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3031` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3032` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3033` | `mcq` | false | `C` | `A. The 1s peak has the lowest energy.` |
| baseline | `mmlu_3034` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3035` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3036` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3037` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3038` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3039` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3040` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3041` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3042` | `mcq` | true | `D` | `D. 251 torr` |
| baseline | `mmlu_3043` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3044` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3045` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3046` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3047` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3048` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3049` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3050` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3051` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3052` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3053` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3054` | `mcq` | false | `B` | `D. 181°C` |
| baseline | `mmlu_3055` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3056` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3057` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3058` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3059` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3060` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3061` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3062` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3063` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3064` | `mcq` | false | `A` | `D. NO3-` |
| baseline | `mmlu_3065` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3066` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3067` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3068` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3069` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3070` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3071` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3072` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3073` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3074` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3075` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3076` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3077` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3078` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3079` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3080` | `mcq` | true | `D` | `D. Sulfur` |
| baseline | `mmlu_3081` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3082` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3083` | `mcq` | false | `C` | `D. Sulfur` |
| baseline | `mmlu_3084` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3085` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3086` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3087` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3088` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3089` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3090` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3091` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3092` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3093` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3094` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3095` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3096` | `mcq` | true | `D` | `D. Making the reaction vessel smaller` |
| baseline | `mmlu_3097` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3098` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3099` | `mcq` | false | `C` | `proton` |
| baseline | `mmlu_3100` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3101` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3102` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3103` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3104` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3105` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3106` | `mcq` | false | `C` | `B. First order` |
| baseline | `mmlu_3107` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3108` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3109` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3110` | `mcq` | false | `D` | `B. HClO` |
| baseline | `mmlu_3111` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3112` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3113` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3114` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3115` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3116` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3117` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3118` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3119` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3120` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3121` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3122` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3123` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3124` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3125` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3126` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3127` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3128` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3129` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3130` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3131` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3132` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3133` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3134` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3135` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3136` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3137` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3138` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3139` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3140` | `mcq` | false | `C` | `A. 1s` |
| baseline | `mmlu_3141` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3142` | `mcq` | true | `C` | `C. Am` |
| baseline | `mmlu_3143` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3144` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3145` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3146` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3147` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3148` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3149` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3150` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3151` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3152` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3153` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3154` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3155` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3156` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3157` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3158` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3159` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3160` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3161` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3162` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3163` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3164` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3165` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3166` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3167` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3168` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3169` | `mcq` | true | `A` | `A. 3.4 × 10^-4 s-1` |
| baseline | `mmlu_3170` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3171` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3172` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3173` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3174` | `mcq` | false | `B` | `D. 7.1 mol` |
| baseline | `mmlu_3175` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3176` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3177` | `mcq` | true | `D` | `D. HBr` |
| baseline | `mmlu_3178` | `mcq` | false | `B` | `A. HNO2` |
| baseline | `mmlu_3179` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3180` | `mcq` | false | `C` | `A. 3+, reduction` |
| baseline | `mmlu_3181` | `mcq` | true | `B` | `B. Rate = k[A]^2` |
| baseline | `mmlu_3182` | `mcq` | false | `C` | `A. 1` |
| baseline | `mmlu_3183` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3184` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3185` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3186` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3187` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3188` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3189` | `mcq` | true | `B` | `B. Only elements that appear in both inputListl and inputList2` |
| baseline | `mmlu_3190` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3191` | `mcq` | false | `B` | `C. Error` |
| baseline | `mmlu_3192` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3193` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3194` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3195` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3196` | `mcq` | true | `C` | `C. Lossless compression` |
| baseline | `mmlu_3197` | `mcq` | true | `A` | `A. isupper()` |
| baseline | `mmlu_3198` | `mcq` | true | `D` | `D. (num MOD 2) = 1` |
| baseline | `mmlu_3199` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3200` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3201` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3202` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3203` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3204` | `mcq` | true | `B` | `B. //` |
| baseline | `mmlu_3205` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3206` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3207` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3208` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3209` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3210` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3211` | `mcq` | true | `A` | `A. Yes` |
| baseline | `mmlu_3212` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3213` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3214` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3215` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3216` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3217` | `mcq` | true | `B` | `B. 1` |
| baseline | `mmlu_3218` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3219` | `mcq` | true | `A` | `A. **` |
| baseline | `mmlu_3220` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3221` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3222` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3223` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3224` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3225` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3226` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3227` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3228` | `mcq` | false | `C` | `8` |
| baseline | `mmlu_3229` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3230` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3231` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3232` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3233` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3234` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3235` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3236` | `mcq` | true | `D` | `D._heads_counter=2` |
| baseline | `mmlu_3237` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3238` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3239` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3240` | `mcq` | false | `C` | `B. Dictionary/map \| Stack \| Queue` |
| baseline | `mmlu_3241` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3242` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3243` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3244` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3245` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3246` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3247` | `mcq` | false | `D` | `A. Error` |
| baseline | `mmlu_3248` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3249` | `mcq` | false | `C` | `D. 4` |
| baseline | `mmlu_3250` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3251` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3252` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3253` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3254` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3255` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3256` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3257` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3258` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3259` | `mcq` | true | `B` | `B. nextAvailableID` |
| baseline | `mmlu_3260` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3261` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3262` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3263` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3264` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3265` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3266` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3267` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3268` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3269` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3270` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3271` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3272` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3273` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3274` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3275` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3276` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3277` | `mcq` | false | `C` | `B. 1 2` |
| baseline | `mmlu_3278` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3279` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3280` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3281` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3282` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3283` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3284` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3285` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3286` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3287` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3288` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3289` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3290` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3291` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3292` | `mcq` | true | `D` | `D. Social Darwinism` |
| baseline | `mmlu_3293` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3294` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3295` | `mcq` | false | `B` | `C. Industrialization` |
| baseline | `mmlu_3296` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3297` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3298` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3299` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3300` | `mcq` | false | `A` | `B. Financial gain` |
| baseline | `mmlu_3301` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3302` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3303` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3304` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3305` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3306` | `mcq` | true | `D` | `D. Poland` |
| baseline | `mmlu_3307` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3308` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3309` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3310` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3311` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3312` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3313` | `mcq` | false | `D` | `B. he wrote in a language that was understandable to the masses, unlike his predecessors has` |
| baseline | `mmlu_3314` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3315` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3316` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3317` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3318` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3319` | `mcq` | true | `B` | `B. Financial gain` |
| baseline | `mmlu_3320` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3321` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3322` | `mcq` | true | `A` | `A. Jean-Jacques Rousseau because he thought society corrupted noble souls.` |
| baseline | `mmlu_3323` | `mcq` | false | `D` | `A. They are "exiled sons" of the British race.` |
| baseline | `mmlu_3324` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3325` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3326` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3327` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3328` | `mcq` | true | `C` | `C. Humanism` |
| baseline | `mmlu_3329` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3330` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3331` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3332` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3333` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3334` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3335` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3336` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3337` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3338` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3339` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3340` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3341` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3342` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3343` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3344` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3345` | `mcq` | false | `C` | `B. New ships like the carrack and caravel` |
| baseline | `mmlu_3346` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3347` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3348` | `mcq` | false | `C` | `B. creating of a secular science to challenge the Church` |
| baseline | `mmlu_3349` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3350` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3351` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3352` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3353` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3354` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3355` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3356` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3357` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3358` | `mcq` | false | `D` | `B. He was so concerned with ceremonies and appearances that he did not rule his country well.` |
| baseline | `mmlu_3359` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3360` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3361` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3362` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3363` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3364` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3365` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3366` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3367` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3368` | `mcq` | true | `C` | `C. Increased disillusionment and cynicism` |
| baseline | `mmlu_3369` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3370` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3371` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3372` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3373` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3374` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3375` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3376` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3377` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3378` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3379` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3380` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3381` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3382` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3383` | `mcq` | true | `D` | `D. Anabaptists` |
| baseline | `mmlu_3384` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3385` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3386` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3387` | `mcq` | true | `C` | `C. general rejection of Catholic dogma` |
| baseline | `mmlu_3388` | `mcq` | true | `B` | `B. People could begin to question the Church on a wider scale.` |
| baseline | `mmlu_3389` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3390` | `mcq` | true | `B` | `B. the consent of those members of society` |
| baseline | `mmlu_3391` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3392` | `mcq` | true | `B` | `B. They were subjugated and destroyed.` |
| baseline | `mmlu_3393` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3394` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3395` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3396` | `mcq` | false | `B` | `C. Increased popular participation in politics` |
| baseline | `mmlu_3397` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3398` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3399` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3400` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3401` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3402` | `mcq` | true | `A` | `A. They initiated an armed resistance against Western interests in Northern China.` |
| baseline | `mmlu_3403` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3404` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3405` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3406` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3407` | `mcq` | true | `C` | `C. Mercantilism` |
| baseline | `mmlu_3408` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3409` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3410` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3411` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3412` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3413` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3414` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3415` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3416` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3417` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3418` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3419` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3420` | `mcq` | true | `B` | `B. France` |
| baseline | `mmlu_3421` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3422` | `mcq` | false | `A` | `B. Article II` |
| baseline | `mmlu_3423` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3424` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3425` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3426` | `mcq` | true | `B` | `B. Religious` |
| baseline | `mmlu_3427` | `mcq` | true | `B` | `B. successfully harnessed the human resources of the new French Republic` |
| baseline | `mmlu_3428` | `mcq` | false | `C` | `A. The switch from a liberal-dominated to a conservative-dominated Parliament` |
| baseline | `mmlu_3429` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3430` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3431` | `mcq` | true | `C` | `C. Mexico` |
| baseline | `mmlu_3432` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3433` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3434` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3435` | `mcq` | true | `D` | `D. Nationalism` |
| baseline | `mmlu_3436` | `mcq` | true | `C` | `C. An increased rate of inflation` |
| baseline | `mmlu_3437` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3438` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3439` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3440` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3441` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3442` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3443` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3444` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3445` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3446` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3447` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3448` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3449` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3450` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3451` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3452` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3453` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3454` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3455` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3456` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3457` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3458` | `mcq` | true | `B` | `B. Replacement level` |
| baseline | `mmlu_3459` | `mcq` | false | `A` | `B. Christianity` |
| baseline | `mmlu_3460` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3461` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3462` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3463` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3464` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3465` | `mcq` | true | `B` | `B. Suburbs` |
| baseline | `mmlu_3466` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3467` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3468` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3469` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3470` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3471` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3472` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3473` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3474` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3475` | `mcq` | true | `C` | `C. Natural` |
| baseline | `mmlu_3476` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3477` | `mcq` | false | `A` | `C. Tertiary` |
| baseline | `mmlu_3478` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3479` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3480` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3481` | `mcq` | false | `B` | `France` |
| baseline | `mmlu_3482` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3483` | `mcq` | true | `C` | `C. Cambodia.` |
| baseline | `mmlu_3484` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3485` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3486` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3487` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3488` | `mcq` | true | `B` | `B. Acculturation.` |
| baseline | `mmlu_3489` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3490` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3491` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3492` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3493` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3494` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3495` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3496` | `mcq` | true | `B` | `B. The Amazon Basin` |
| baseline | `mmlu_3497` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3498` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3499` | `mcq` | true | `B` | `B` |
