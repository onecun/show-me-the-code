# -*- coding:utf-8 -*-
#第一版，没有对大文件进行优化

from collections import Counter
import re

with open('f.txt', 'r') as f:
    f1 = re.sub(r'[.,?!]', ' ', f.read()) #用正则把标点换成空格

f1 = f1.lower()
word_list = f1.split()
word_dict = dict(Counter(word_list)) #使用Couter计数
for k, v in word_dict.items():
    print(k,':', v)