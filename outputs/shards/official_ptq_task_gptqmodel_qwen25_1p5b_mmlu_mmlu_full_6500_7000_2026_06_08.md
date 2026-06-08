# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 309 / 500 | 0.6180 | 8.7528 | 0.168947 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_6500` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6501` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6502` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6503` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6504` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6505` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6506` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6507` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6508` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6509` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6510` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6511` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6512` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6513` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6514` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6515` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6516` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6517` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6518` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6519` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6520` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6521` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6522` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6523` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6524` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6525` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6526` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6527` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6528` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6529` | `mcq` | false | `B` | `A. Recognition of governments is very prevalent in contemporary practice` |
| baseline | `mmlu_6530` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6531` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6532` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6533` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6534` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6535` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6536` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6537` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6538` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6539` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6540` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6541` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6542` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6543` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6544` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6545` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6546` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6547` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6548` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6549` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6550` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6551` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6552` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6553` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6554` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6555` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6556` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6557` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6558` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6559` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6560` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6561` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6562` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6563` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6564` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6565` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6566` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6567` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6568` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6569` | `mcq` | true | `A` | `A. Law and Economics` |
| baseline | `mmlu_6570` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6571` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6572` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6573` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6574` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6575` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6576` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6577` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6578` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6579` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6580` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6581` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6582` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6583` | `mcq` | true | `B` | `B. Positive law.` |
| baseline | `mmlu_6584` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6585` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6586` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6587` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6588` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6589` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6590` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6591` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6592` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6593` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6594` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6595` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_6596` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6597` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6598` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6599` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6600` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6601` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6602` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6603` | `mcq` | false | `B` | `D. He rejects the idea of equality.` |
| baseline | `mmlu_6604` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6605` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6606` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6607` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6608` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6609` | `mcq` | true | `C` | `C. Because Aristotle believed that man is a 'social animal'` |
| baseline | `mmlu_6610` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6611` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6612` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6613` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6614` | `mcq` | true | `A` | `A. Legal fiction` |
| baseline | `mmlu_6615` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6616` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6617` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6618` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6619` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6620` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6621` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6622` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6623` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6624` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6625` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6626` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6627` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6628` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6629` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6630` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6631` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6632` | `mcq` | false | `B` | `A. Because of their vagueness.` |
| baseline | `mmlu_6633` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6634` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6635` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6636` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6637` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6638` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6639` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6640` | `mcq` | false | `A` | `D. None of the above` |
| baseline | `mmlu_6641` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6642` | `mcq` | true | `A` | `A. interpret` |
| baseline | `mmlu_6643` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6644` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6645` | `mcq` | true | `A` | `A. Because it fails to address the actual capabilities people have to benefit from his theory of justice.` |
| baseline | `mmlu_6646` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6647` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6648` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6649` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6650` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6651` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6652` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6653` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6654` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6655` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6656` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6657` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6658` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6659` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6660` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6661` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6662` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6663` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6664` | `mcq` | true | `B` | `B. Sanction.` |
| baseline | `mmlu_6665` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6666` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6667` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6668` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6669` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6670` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6671` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6672` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6673` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6674` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6675` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6676` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6677` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6678` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6679` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6680` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6681` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6682` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6683` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6684` | `mcq` | false | `D` | `A. Equivocation` |
| baseline | `mmlu_6685` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6686` | `mcq` | false | `B` | `C. Hypostatization` |
| baseline | `mmlu_6687` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6688` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6689` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6690` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6691` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6692` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6693` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6694` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6695` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6696` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6697` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6698` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6699` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6700` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6701` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6702` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6703` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6704` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6705` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6706` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6707` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6708` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6709` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6710` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6711` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6712` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6713` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6714` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6715` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6716` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6717` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6718` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6719` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6720` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6721` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6722` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6723` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6724` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6725` | `mcq` | true | `A` | `A. no valid conclusion can be drawn` |
| baseline | `mmlu_6726` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6728` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6729` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6730` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6731` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6732` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6733` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6734` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6735` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6736` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6737` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6738` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6739` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6740` | `mcq` | true | `D` | `D. Style over substance` |
| baseline | `mmlu_6741` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6742` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6743` | `mcq` | false | `B` | `A. no valid conclusion can be drawn` |
| baseline | `mmlu_6744` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6745` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6746` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6747` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6748` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6749` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6750` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6751` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6752` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6753` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6754` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6755` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6756` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6757` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6758` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6759` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6760` | `mcq` | true | `C` | `C. irrelevant conclusion` |
| baseline | `mmlu_6761` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6762` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6763` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6764` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6765` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6766` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6767` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6768` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6769` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6770` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6771` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6772` | `mcq` | true | `B` | `B. Equivocation` |
| baseline | `mmlu_6773` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6774` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6775` | `mcq` | true | `D` | `D. Loaded language` |
| baseline | `mmlu_6776` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6777` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6778` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6779` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6780` | `mcq` | true | `A` | `A. Equivocation` |
| baseline | `mmlu_6781` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6782` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6783` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6784` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6785` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6786` | `mcq` | false | `A` | `D. both A and B` |
| baseline | `mmlu_6787` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6788` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6789` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6790` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6791` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6792` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6793` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6794` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6795` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6796` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6797` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6798` | `mcq` | true | `A` | `A. Equivocation` |
| baseline | `mmlu_6799` | `mcq` | false | `B` | `A. Argument from Ignorance` |
| baseline | `mmlu_6800` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6801` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6802` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6803` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6804` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6805` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6806` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6807` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6808` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6809` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_6810` | `mcq` | true | `D` | `D. Argument from Ignorance` |
| baseline | `mmlu_6811` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6812` | `mcq` | true | `D` | `D. Equivocation` |
| baseline | `mmlu_6813` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6814` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6815` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6816` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6817` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6818` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6819` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6820` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6821` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6822` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6823` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6824` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6825` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6826` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6827` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6828` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6829` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6830` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6831` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6832` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6833` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6834` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6835` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6836` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6837` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6838` | `mcq` | false | `D` | `C. 48` |
| baseline | `mmlu_6839` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6840` | `mcq` | false | `B` | `D. False, True` |
| baseline | `mmlu_6841` | `mcq` | true | `A` | `A. O(D)` |
| baseline | `mmlu_6842` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6843` | `mcq` | true | `C` | `C. 8` |
| baseline | `mmlu_6844` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6845` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6846` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6847` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6848` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6849` | `mcq` | true | `B` | `B. not pure` |
| baseline | `mmlu_6850` | `mcq` | false | `B` | `C. True, False` |
| baseline | `mmlu_6851` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6852` | `mcq` | true | `A` | `A. The number of hidden nodes` |
| baseline | `mmlu_6853` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6854` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6855` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6856` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6857` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6858` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6859` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6860` | `mcq` | false | `A` | `D. False, True` |
| baseline | `mmlu_6861` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6862` | `mcq` | false | `C` | `B. linear in N` |
| baseline | `mmlu_6863` | `mcq` | true | `D` | `D. Decrease variance` |
| baseline | `mmlu_6864` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6865` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6866` | `mcq` | false | `C` | `D. None of the above` |
| baseline | `mmlu_6867` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6868` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6869` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6870` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6871` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6872` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6873` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6874` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6875` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6876` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6877` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6878` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6879` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6880` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6881` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6882` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6883` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6884` | `mcq` | true | `D` | `D. False, True` |
| baseline | `mmlu_6885` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6886` | `mcq` | false | `A` | `C. True, False` |
| baseline | `mmlu_6887` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6888` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6889` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6890` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6891` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6892` | `mcq` | true | `D` | `D. False, True` |
| baseline | `mmlu_6893` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6894` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6895` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6896` | `mcq` | false | `A` | `D. False, True` |
| baseline | `mmlu_6897` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6898` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6899` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6900` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6901` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6902` | `mcq` | false | `A` | `D. False, True` |
| baseline | `mmlu_6903` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6904` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6905` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6906` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6907` | `mcq` | false | `B` | `D. False, True` |
| baseline | `mmlu_6908` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6909` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6910` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6911` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6912` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6913` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6914` | `mcq` | true | `D` | `D. False, True` |
| baseline | `mmlu_6915` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6916` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6917` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6918` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6919` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6920` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6921` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6922` | `mcq` | true | `C` | `C. True, False` |
| baseline | `mmlu_6923` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6924` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6925` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6926` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6927` | `mcq` | false | `B` | `D. Both` |
| baseline | `mmlu_6928` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6929` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6930` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6931` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6932` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6933` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6934` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6935` | `mcq` | false | `B` | `D. All of above` |
| baseline | `mmlu_6936` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6937` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6938` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6939` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6940` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6941` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6942` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6943` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6944` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6945` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6946` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6947` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6948` | `mcq` | true | `D` | `D. Heuristics` |
| baseline | `mmlu_6949` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6950` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6951` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6952` | `mcq` | true | `B` | `B. Work schedule design.` |
| baseline | `mmlu_6953` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6954` | `mcq` | true | `D` | `D. Legitimate` |
| baseline | `mmlu_6955` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6956` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6957` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6958` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6959` | `mcq` | false | `A` | `D. Developmental` |
| baseline | `mmlu_6960` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6961` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6962` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6963` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6964` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6965` | `mcq` | false | `C` | `B. Shaper` |
| baseline | `mmlu_6966` | `mcq` | false | `D` | `C. Financial planning` |
| baseline | `mmlu_6967` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6968` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6969` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6970` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6971` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6972` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6973` | `mcq` | true | `A` | `A. John Stuart Mill` |
| baseline | `mmlu_6974` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6975` | `mcq` | false | `B` | `Independent` |
| baseline | `mmlu_6976` | `mcq` | false | `D` | `B. Divisional` |
| baseline | `mmlu_6977` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6978` | `mcq` | true | `D` | `D. Socialisation` |
| baseline | `mmlu_6979` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6980` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6981` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6982` | `mcq` | false | `B` | `Video conference` |
| baseline | `mmlu_6983` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6984` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6985` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6986` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6987` | `mcq` | true | `B` | `B. A formal process of planning to fill a role that will become vacant.` |
| baseline | `mmlu_6988` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6989` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6990` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6991` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6992` | `mcq` | true | `C` | `C. Social audit` |
| baseline | `mmlu_6993` | `mcq` | false | `B` | `A. Task culture` |
| baseline | `mmlu_6994` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6995` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6996` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6997` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6998` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6999` | `mcq` | true | `C` | `C` |
