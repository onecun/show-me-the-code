# 生成一个验证码图片
# coding: UTF-8

import random, string
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def drawImg(txt, font_path):
    width = 240
    height = 60
    # 创建图片
    img = Image.new('RGB', (width, height), (180, 180, 180))
    font = ImageFont.truetype(font_path, 60)
    # 把图像作为画板
    draw = ImageDraw.Draw(img)
    # 写字
    for k in range(4):
        draw.text((60*k+10, 0), txt[k], font = font, fill = color())
    # 在背景画点
    for l in range(random.randint(1500,3000)):
        draw.point((random.randint(0,width), random.randint(0,height)), fill = color())
    # 模糊整个图片
    img = img.filter(ImageFilter.BLUR)
    img.save("".join(txt) + '.png' or '.jpg');

def color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))    

def main():
    font_path = r'C:\Users\pp\Documents\Python\show_my_code\0\myfont.ttf'
    txt = [random.choice(string.ascii_letters) for i in range(4)]
    drawImg(txt, font_path)

if __name__ == '__main__':
    main()