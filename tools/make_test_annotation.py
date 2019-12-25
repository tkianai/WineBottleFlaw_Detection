
import os
import os.path as osp
import argparse
import json
from PIL import Image


def parse_args():

    parser = argparse.ArgumentParser(description='Make test annotation')
    parser.add_argument('--img', type=str,
                        default='./datasets/chongqing1_round1_testA_20191223/images', help='test images directory')
    parser.add_argument(
        '--save', type=str, default='./datasets/chongqing1_round1_testA_20191223/test_annotations.json', help='save path')
    parser.add_argument('--train', type=str,
                        default='./datasets/chongqing1_round1_train1_20191223/train_annotations.json', help='train annotation file')

    args = parser.parse_args()
    save_dir = osp.dirname(args.save)
    if not osp.exists(save_dir):
        os.makedirs(save_dir)

    return args


def is_valid(filename):
    EXTENSION = ('.jpg', '.png')
    return filename.endswith(EXTENSION)


def main(args):

    train_data = json.load(open(args.train))

    test_data = {
        'info': train_data['info'],
        'license': train_data['license'],
        'categories': train_data['categories'],
        'images': [],
        'annotations': []
    }

    img_id = 1
    for imgname in os.listdir(args.img):
        if not is_valid(imgname):
            continue
        
        img = Image.open(osp.join(args.img, imgname))
        width, height = img.size
        item = {
            'file_name': imgname,
            'height': height,
            'width': width,
            'id': img_id
        }
        test_data['images'].append(item)
        img_id += 1

    # save results
    with open(args.save, 'w') as w_obj:
        json.dump(test_data, w_obj)
    

if __name__ == "__main__":
    args = parse_args()
    main(args)
