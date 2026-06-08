# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 321 / 500 | 0.6420 | 8.1995 | 0.181448 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_3500` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3501` | `mcq` | false | `D` | `B. Italy` |
| baseline | `mmlu_3502` | `mcq` | false | `C` | `A. First` |
| baseline | `mmlu_3503` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3504` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3505` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3506` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3507` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3508` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3509` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3510` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3511` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3512` | `mcq` | true | `C` | `C. Agglomeration.` |
| baseline | `mmlu_3513` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3514` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3515` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3516` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3517` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3518` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3519` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3520` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3521` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3522` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3523` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3524` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3525` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3526` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3527` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3528` | `mcq` | true | `B` | `B. The end of the Cold War` |
| baseline | `mmlu_3529` | `mcq` | true | `B` | `B. Air` |
| baseline | `mmlu_3530` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3531` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3532` | `mcq` | true | `C` | `C. Indo-European` |
| baseline | `mmlu_3533` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3534` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3535` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3536` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3537` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3538` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3539` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3540` | `mcq` | true | `C` | `C. Information` |
| baseline | `mmlu_3541` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3542` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3543` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3544` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3545` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3546` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3547` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3548` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3549` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3550` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3551` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3552` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3553` | `mcq` | true | `A` | `A. defend North America and Western Europe against the threat of communism.` |
| baseline | `mmlu_3554` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3555` | `mcq` | false | `C` | `B. Contagious` |
| baseline | `mmlu_3556` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3557` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3558` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3559` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3560` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3561` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3562` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3563` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3564` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3565` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3566` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3567` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3568` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3569` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3570` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3571` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3572` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3573` | `mcq` | true | `D` | `D. Indo-European` |
| baseline | `mmlu_3574` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3575` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3576` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3577` | `mcq` | true | `C` | `C. Chile` |
| baseline | `mmlu_3578` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3579` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3580` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3581` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3582` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3583` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3584` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3585` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3586` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3587` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3588` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3589` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3590` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3591` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3592` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3593` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3594` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3595` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3596` | `mcq` | true | `A` | `A./core, periphery, and semi-periphery./` |
| baseline | `mmlu_3597` | `mcq` | false | `C` | `B. Iraq` |
| baseline | `mmlu_3598` | `mcq` | true | `D` | `D. Spain` |
| baseline | `mmlu_3599` | `mcq` | false | `C` | `B. East Asia` |
| baseline | `mmlu_3600` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3601` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3602` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3603` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3604` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3605` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3606` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3607` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3608` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3609` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3610` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3611` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3612` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3613` | `mcq` | false | `C` | `E.` |
| baseline | `mmlu_3614` | `mcq` | false | `B` | `C. Pesticides` |
| baseline | `mmlu_3615` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3616` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3617` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3618` | `mcq` | false | `D` | `B. Land use` |
| baseline | `mmlu_3619` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3620` | `mcq` | false | `C` | `B. Secesion` |
| baseline | `mmlu_3621` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3622` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3623` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3624` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3625` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3626` | `mcq` | true | `C` | `C. China` |
| baseline | `mmlu_3627` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3628` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3629` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3630` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3631` | `mcq` | false | `A` | `B. Asia` |
| baseline | `mmlu_3632` | `mcq` | true | `B` | `B. Christianity` |
| baseline | `mmlu_3633` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3634` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3635` | `mcq` | true | `B` | `B. Transport` |
| baseline | `mmlu_3636` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3637` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3638` | `mcq` | true | `B` | `B. English.` |
| baseline | `mmlu_3639` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3640` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3641` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3642` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3643` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3644` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3645` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3646` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3647` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3648` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3649` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3650` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3651` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3652` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3653` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3654` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3655` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3656` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3657` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3658` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3659` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3660` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3661` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3662` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3663` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3664` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3665` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3666` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3667` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3668` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3669` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3670` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3671` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3672` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3673` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3674` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3675` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3676` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3677` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3678` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3679` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3680` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3681` | `mcq` | false | `C` | `B. I and IV only` |
| baseline | `mmlu_3682` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3683` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3684` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3685` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3686` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3687` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3688` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3689` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3690` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3691` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3692` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3693` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3694` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3695` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3696` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3697` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3698` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3699` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3700` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3701` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3702` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3703` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3704` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3705` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3706` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3707` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3708` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3709` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3710` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3711` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3712` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3713` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3714` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3715` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3716` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3717` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3718` | `mcq` | false | `C` | `B. Congress` |
| baseline | `mmlu_3719` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3720` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3721` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3722` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3723` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3724` | `mcq` | true | `A` | `A. judicial activism` |
| baseline | `mmlu_3725` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3726` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3728` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3729` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3730` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3731` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3732` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3733` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3734` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3735` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3736` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3737` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3738` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3739` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3740` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3741` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3742` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3743` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3744` | `mcq` | true | `C` | `C. reduce the federal deficit` |
| baseline | `mmlu_3745` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3746` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3747` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3748` | `mcq` | true | `A` | `A. determine both the rules of the House and conditions for legislative process.` |
| baseline | `mmlu_3749` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3750` | `mcq` | false | `C` | `D. II and III only` |
| baseline | `mmlu_3751` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3752` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3753` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3754` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3755` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3756` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3757` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3758` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3759` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3760` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3761` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3762` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3763` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3764` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3765` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3766` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3767` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3768` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3769` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3770` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3771` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3772` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3773` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3774` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3775` | `mcq` | true | `A` | `A. will review a lower court decision.` |
| baseline | `mmlu_3776` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3777` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3778` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3779` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3780` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3781` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3782` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3783` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3784` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3785` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3786` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3787` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3788` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3789` | `mcq` | true | `C` | `C. Federal budget entitlements` |
| baseline | `mmlu_3790` | `mcq` | false | `B` | `D. Cabinet` |
| baseline | `mmlu_3791` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3792` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3793` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3794` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3795` | `mcq` | true | `C` | `C. Increasing concentration of ownership in the news media` |
| baseline | `mmlu_3796` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3797` | `mcq` | true | `D` | `D. president` |
| baseline | `mmlu_3798` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3799` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3800` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3801` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3802` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3803` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3804` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3805` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3806` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3807` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3808` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3809` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3810` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3811` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3812` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3813` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3814` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3815` | `mcq` | true | `D` | `D. I, II, and IV only` |
| baseline | `mmlu_3816` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3817` | `mcq` | true | `B` | `B. Ways and Means` |
| baseline | `mmlu_3818` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3819` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3820` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3821` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3822` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3823` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3824` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3825` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3826` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3827` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3828` | `mcq` | true | `D` | `D. John Locke` |
| baseline | `mmlu_3829` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3830` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3831` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3832` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3833` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3834` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3835` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3836` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3837` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3838` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3839` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3840` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3841` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3842` | `mcq` | true | `B` | `B. contractionary monetary policy.` |
| baseline | `mmlu_3843` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3844` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3845` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3846` | `mcq` | true | `D` | `D. Opportunity Cost` |
| baseline | `mmlu_3847` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3848` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3849` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3850` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3851` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3852` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3853` | `mcq` | true | `B` | `B. 30%. Explanation: The reserve ratio can be calculated as follows:  Reserve Ratio = (Excess Reserves / Deposits) * 100` |
| baseline | `mmlu_3854` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3855` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3856` | `mcq` | false | `B` | `D. Expected future inflation.` |
| baseline | `mmlu_3857` | `mcq` | true | `B` | `B. inflation.` |
| baseline | `mmlu_3858` | `mcq` | true | `D` | `D. I II and III are correct.` |
| baseline | `mmlu_3859` | `mcq` | false | `A` | `D. Falls     Falls     No change     No change` |
| baseline | `mmlu_3860` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3861` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3862` | `mcq` | true | `B` | `B. Dollar bills` |
| baseline | `mmlu_3863` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3864` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3865` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3866` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3867` | `mcq` | false | `B` | `A. Decreases            Increases      Decreases` |
| baseline | `mmlu_3868` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3869` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3870` | `mcq` | true | `D` | `D. unexpectedly higher resource prices.` |
| baseline | `mmlu_3871` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3872` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3873` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3874` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3875` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3876` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3877` | `mcq` | false | `C` | `D. $5,000` |
| baseline | `mmlu_3878` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3879` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3880` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3881` | `mcq` | false | `D` | `A. increase by $2.9 million.` |
| baseline | `mmlu_3882` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3883` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3884` | `mcq` | true | `B` | `B. 7 14` |
| baseline | `mmlu_3885` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3886` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3887` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3888` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3889` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3890` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3891` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3892` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3893` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3894` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3895` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3896` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3897` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3898` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3899` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3900` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3901` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3902` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3903` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3904` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3905` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3906` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3907` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3908` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3909` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3910` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3911` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3912` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3913` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3914` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3915` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3916` | `mcq` | false | `D` | `A. The productivity of labor in country Z is 33 percent higher than in country X.` |
| baseline | `mmlu_3917` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3918` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3919` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3920` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3921` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3922` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3923` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3924` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3925` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3926` | `mcq` | true | `D` | `D. dumping.` |
| baseline | `mmlu_3927` | `mcq` | false | `C` | `B. $1 million` |
| baseline | `mmlu_3928` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3929` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3930` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3931` | `mcq` | false | `B` | `C. 50 percent.` |
| baseline | `mmlu_3932` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3933` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3934` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3935` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3936` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3937` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3938` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3939` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3940` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3941` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3942` | `mcq` | true | `C` | `C. expansionary monetary policy` |
| baseline | `mmlu_3943` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3944` | `mcq` | false | `B` | `C. variable.` |
| baseline | `mmlu_3945` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3946` | `mcq` | false | `D` | `C. $1.75` |
| baseline | `mmlu_3947` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3948` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3949` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3950` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3951` | `mcq` | true | `D` | `D. I and II` |
| baseline | `mmlu_3952` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3953` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3954` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3955` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3956` | `mcq` | true | `B` | `B. $400 billion` |
| baseline | `mmlu_3957` | `mcq` | true | `B` | `B. Imports.` |
| baseline | `mmlu_3958` | `mcq` | false | `A` | `D. Increased government spending.` |
| baseline | `mmlu_3959` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3960` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3961` | `mcq` | false | `D` | `C. Sell bonds   Decreases   Decreases   Inflation` |
| baseline | `mmlu_3962` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3963` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3964` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3965` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3966` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3967` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3968` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3969` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3970` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3971` | `mcq` | false | `B` | `A. raise the price level and output in the economy.` |
| baseline | `mmlu_3972` | `mcq` | false | `C` | `D. China ($2).` |
| baseline | `mmlu_3973` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3974` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3975` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3976` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3977` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3978` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3979` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3980` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3981` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3982` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3983` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3984` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3985` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3986` | `mcq` | true | `A` | `A. implementing innovative production techniques.` |
| baseline | `mmlu_3987` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3988` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3989` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3990` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3991` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3992` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3993` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3994` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3995` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3996` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3997` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3998` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3999` | `mcq` | true | `B` | `B` |
