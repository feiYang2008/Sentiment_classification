# -*- coding: UTF-8 -*-
import os
from collections import Counter
import pandas as pd

def get_counter(data):
    '''
    :param data: 可迭代对象，每个data是以空格为间隔的单词组成的句子
    :return:
    '''
    lens = []
    for i in range(len(data)):
        line = str(data[i]).strip()
        line = line.split(' ')
        temp_len = len(line)
        lens.append(temp_len)
    len_counter = Counter(lens)

    return len_counter


def get_percent(data, targ_len, len_counter):
    n = 0
    # len_counter = get_counter(data)

    for k, v in len_counter.items():
        if k <= targ_len:
            n += v

    return n / len(data)

def get_required_len(data, targ_percent):
    len_counter = get_counter(data)
    for len in range(max(len_counter)):
        percent = get_percent(data, len, len_counter)
        if percent >= targ_percent:
            return len
    print('wrong percent!')
    return None


if __name__ == '__main__':
    root_path = os.path.abspath('./')
    valid_path = os.path.join(root_path, 'dataset', 'valid.csv')
    train_path = os.path.join(root_path, 'dataset', 'train.csv')

    valid = pd.read_csv(valid_path)
    train = pd.read_csv(train_path)

    len_train_input = get_required_len(train['content_cut_del_stopwords'], 0.98)
    len_valid_output = get_required_len(valid['content_cut_del_stopwords'], 0.98)
    print(len_train_input, len_valid_output)








