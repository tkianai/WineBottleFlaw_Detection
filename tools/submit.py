
import os
import os.path as osp
import argparse
import json

def parse_args():

    parser = argparse.ArgumentParser(description='Make submit style prediction from other framework')
    parser.add_argument('--data', type=str, help='detection results')
    parser.add_argument('--mode', type=str, default='mmdet', help='detection results from which framework [mmdet, maskrcnn, self]')
    parser.add_argument('--test', type=str, default='./datasets/chongqing1_round1_testA_20191223/test_annotations.json', help='test annotation file')
    parser.add_argument('--save', type=str, default='./submit.json', help='save path')

    args = parser.parse_args()
    save_dir = osp.dirname(args.save)
    if not osp.exists(save_dir):
        os.makedirs(save_dir)
    
    return args

def main(args):

    test_data = json.load(open(args.test))
    results = json.load(open(args.data))
    submit_data = {
        'images': [],
        'annotations': []
    }

    for item in test_data['images']:
        _s_item = {
            'file_name': item['file_name'],
            'id': item['id']
        }
        submit_data['images'].append(_s_item)

    if args.mode == 'mmdet' or args.mode == 'maskrcnn':
        submit_data['annotations'] = results
    else:
        raise ValueError("Do not support mode [{}]".format(args.mode))


    # save
    with open(args.save, 'w') as w_obj:
        json.dump(submit_data, w_obj)


if __name__ == "__main__":
    args = parse_args()
    main(args)
