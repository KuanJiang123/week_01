from __future__ import division

import re
import jieba
from collections import Counter

filename = 'train.txt'
def get_data(filename):
    f = open(filename, 'r', encoding='utf-8')
    line = f.readline()
    data = ''
    while line:
        sent = re.findall(u"[\u4e00-\u9fa5]+", line)
        data += ','.join(sent)
        line = f.readline()
    return data

def cut(data):
    return list(jieba.cut(data))

def _2_gram(data):
    return [data[i]+data[i+1] for i in range(len(data)-1)]

def get_gram_count(word, wc):
    if word in wc: return wc[word]
    else: return wc.most_common()[-1][-1]

data = get_data(filename)
data = cut(data)
_1_gram = Counter(data)
_2_gram = Counter(_2_gram(data))

def _2_gram_model(sentence):
    sent = cut(sentence)
    pro = 1
    for i in range(len(sent)-1):
        two_count = get_gram_count(sent[i] + sent[i+1], _2_gram)
        one_count = get_gram_count(sent[i], _1_gram)
        pro *= (two_count/one_count)
    return pro

pro = _2_gram_model('旅行者保险有租赁保险吗')
print(pro)



