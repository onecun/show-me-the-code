# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
# -*- coding:utf-8 -*-

from collections import Counter
import re
import os

def getFile(path):
    f = ''
    # 遍历目录 os.walk() 返回三个值，分别为：目录地址，地址下的文件夹名称，文件名
    for dirpath, dirnames, filenames in os.walk(path):
        for f_name in filenames:
            f_dir = os.path.join(dirpath, f_name)
            f = f + str(determineTxt(f_dir, f_name))
    return f

def determineTxt(f_dir, f_name):
    # 分离拓展名和文件名 os.path.splitext() 返回 ['文件名'， '后缀']
    postfix = os.path.splitext(f_name)[1]
    txt_name = os.path.splitext(f_name)[0]
    # 判断是否为文档
    if postfix == '.txt': 
        f = joinWords(f_dir, txt_name)
        return f

def joinWords(f_dir, txt_name):
    # 获取内容
    with open(f_dir) as f_txt:
        f = f_txt.read()
    return f

def conterWords(f):
    f1 = re.sub(r'[.,?!]', ' ', f)
    f1 = f1.lower()
    word_list = f1.split()
    word_dict = dict(Counter(word_list))
    # 找到最大数目
    max_v = 0
    for k, v in word_dict.items():
        if v >= max_v:
            max_v = v
    # 输出次数最多的词
    for k, v in word_dict.items():
        if v == max_v:
            print(r'出现次数最多的词是："%s" ,共出现 "%s" 次'%(k, v))
    
def main():
    path = r'C:\Users\pp\Documents\Python\show_my_code\6'
    f = getFile(path)
    conterWords(f)

if __name__ == '__main__':
    main()