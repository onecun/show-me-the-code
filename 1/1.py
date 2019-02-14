#-*- coding:utf-8 -*-

import string,random
def createKeys(num, lenth):
    f = open('keys.txt', 'w')
    chars = string.ascii_letters + string.digits #生成所有字母和数字
    for i in range(num):
        l = [random.choice(chars) for j in range(lenth)]
        #这条语句等同于：
        #l = []
        #for j in range(lenth):
        #   s = random.choice(chars) #从chars中随机选取一个字符
        #   l.append(s)

        f.write('{}\n'.format(''.join(l))) #使用format进行格式化，join只对字符操作
    f.close()

if __name__ == '__main__':
    createKeys(200, 12)