
import os
import argparse
import torch
from collections import OrderedDict


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model')
    parser.add_argument('--save')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    pretrained = torch.load(args.model)['model']
    remove_keys = ['cls_logits']
    trimed = {
        "model": OrderedDict()
    }
    for key, value in pretrained.items():
        skip = False
        for r_k in remove_keys:
            if r_k in key:
                print(key)
                skip = True
                break
        
        if not skip:
            trimed['model'][key] = value
        
    torch.save(trimed, args.save)

if __name__ == "__main__":
    main()
