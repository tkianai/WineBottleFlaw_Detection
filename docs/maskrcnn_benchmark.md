# Records

| model                             | iters | lr   | batch size | pretrained | mAP   | score   | tta     | -                         |
| --------------------------------- | ----- | ---- | ---------- | ---------- | ----- | ------- | ------- | ------------------------- |
| fcos_imprv_dcnv2_X_101_64x4d_FPN  | 6k    | 0.01 | 24         | yes        | 0.518 | 0.76977 | 0.76977 | -                         |
| fcos_imprv_dcnv2_X_101_64x4d_FPN  | 6k    | 0.01 | 24         | yes        | 0.548 | 0.76977 | -       | vertical augment          |
| fcos_imprv_dcnv2_X_101_64x4d_FPN  | 9k    | 0.01 | 8          | yes        | 0.553 | 0.76977 | -       | larger size train, longer |
| fcos_syncbn_bs32_c128_ms_MNV2_FPN | 9k    | 0.01 | 8          | yes        | 0.4978     | -       | -       | longer                    |