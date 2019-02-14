# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
# -*- coding:utf-8 -*-

import os 
from PIL import Image

def getFile(path):
    # 遍历目录 os.walk() 返回三个值，分别为：目录地址，地址下的目录名称，文件名
    for dirpath, dirnames, filenames in os.walk(path):
        for f_name in filenames:
            f_dir = os.path.join(dirpath, f_name)
            determineImage(f_dir, f_name)

def determineImage(f_dir, f_name):
        # 分离拓展名和文件名 os.path.splitext() 返回 ['文件名'， '后缀']
        postfix = os.path.splitext(f_name)[1]
        img_name = os.path.splitext(f_name)[0]
        # 判断是否为图片
        if postfix == '.png' or postfix == '.jpg': 
            resizeImage(f_dir, img_name)

def resizeImage(f_dir, img_name):
    img = Image.open(f_dir)
    # 重置图片大小
    new_img = img.resize((1136, 640), Image.ANTIALIAS)
    # 设置新文件名称，保存 
    new_name = '{0}.png'.format(img_name)
    new_img.save('new_'+new_name)

def main():
    path = r'C:\Users\pp\Pictures'
    getFile(path)

if __name__ == '__main__':
    main()