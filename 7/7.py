#  有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
# 优化了 6.py 里函数重重嵌套的问题
# 计数不准确，原因未知，待改
# -*- coding:utf-8 -*-

import re
import os

def getFile(path):
    f_dict = {}
    # 遍历目录 os.walk() 返回三个值，分别为：目录地址，地址下的文件夹名称，文件名
    for dirpath, dirnames, filenames in os.walk(path):
        for f_name in filenames:
            f_dir = os.path.join(dirpath, f_name)
            f_dict[f_name] = f_dir
    return f_dict

def determineCode(f_name):
    # 分离拓展名和文件名 os.path.splitext() 返回 ['文件名'， '后缀']
    postfix = os.path.splitext(f_name)[1]
    # 判断是否为代码
    if postfix == '.py': 
        return True

def counterLine(f_dir):
    # 获取内容
    with open(f_dir, 'r', encoding='UTF-8') as f_txt:
        f_line = f_txt.readlines()
    num_code, num_empty, num_blank = 0, 0, 0
    # 数数
    for i in f_line:
        num_code += 1
        if i.strip() == '':
            num_blank += 1
        if i[0] == r'#':
            num_empty += 1
    return num_code, num_blank, num_empty

def main():
    path = r'C:\Users\pp\Documents\Python'
    f_dict = getFile(path)
    nc, nb, ne = 0, 0, 0
    for i in f_dict:
        if determineCode(i):
            c, b, e = counterLine(f_dict[i])
        nc = nc + c
        nb = nb + b
        ne = ne + e
    print('code: %d , blank: %d , empty: %d'%(nc, nb/2, ne))

if __name__ == '__main__':
    main()