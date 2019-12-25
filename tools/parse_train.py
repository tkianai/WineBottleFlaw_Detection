
import os
import json
import random
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Split train into train/val')
    parser.add_argument('--data', type=str, default='./datasets/chongqing1_round1_train1_20191223/coco_annotations.json', help='annotation file path')
    parser.add_argument('--ratio', type=float, default=0.1, help='Val/Total ratio')
    parser.add_argument(
        '--save', type=str, default='./datasets/chongqing1_round1_train1_20191223/', help='save directory')
    
    args = parser.parse_args()
    if not os.path.join(args.save):
        os.makedirs(args.save)
    return args


def main(args):

    total_data = json.load(open(args.data))
    img_ids = []
    for item in total_data['images']:
        img_ids.append(item['id'])
    random.shuffle(img_ids)
    
    val_num = int(len(img_ids) * args.ratio)
    val_ids = set(img_ids[:val_num])
    train_ids = set(img_ids[val_num:])

    train_data = {
        'info': total_data['info'],
        'license': total_data['license'],
        'categories': total_data['categories'],
        'images': [],
        'annotations': []
    }
    val_data = {
        'info': total_data['info'],
        'license': total_data['license'],
        'categories': total_data['categories'],
        'images': [],
        'annotations': []
    }

    for item in total_data['images']:
        if item['id'] in val_ids:
            val_data['images'].append(item)
        else:
            train_data['images'].append(item)
    
    for item in total_data['annotations']:
        if item['image_id'] in val_ids:
            val_data['annotations'].append(item)
        else:
            train_data['annotations'].append(item)
    
    # save result
    with open(os.path.join(args.save, 'train_annotations.json'), 'w') as w_obj:
        json.dump(train_data, w_obj)
    with open(os.path.join(args.save, 'val_annotations.json'), 'w') as w_obj:
        json.dump(val_data, w_obj)


if __name__ == "__main__":
    args = parse_args()
    main(args)
