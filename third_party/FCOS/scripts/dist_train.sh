#!/bin/sh

python -m torch.distributed.launch --nproc_per_node=8 tools/train_net.py --config-file configs/bottlewine/fcos_imprv_dcnv2_X_101_64x4d_FPN_2x.yaml