#-*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
def imgAddNum(addr, ft, name, str):
    #加载图片
    im = Image.open(addr) 
    x, y = im.size
    #设置位置
    fontsize = y/1
    position = x - fontsize 
    #获取字体
    myfont = ImageFont.truetype("myfont.ttf", ft) 
    #写字
    ImageDraw.ImageDraw(im).text((position, 0), str, fill='red', font=myfont)
    #保存
    im.save(name) 

if __name__ == '__main__':
    imgAddNum(r'me.png', 30, r'c.png', '5')