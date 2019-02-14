#11 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
#12 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
#coding: UTF-8

def filter():
    s = []
    f = open('sensitive.txt', 'r')
    for i in f.readlines():
        if '\n' in i:
            s.append(i[:-1])
        else:
            s.append(i)
    f.close()
    return s

def get_words():
    words = input('说吧：')
    return words

def main_11():
    s = filter()
    words = get_words()
    a = False
    for i in s:
        if words.find(i) > -1:
            a = True
    if a:
        print('freedom')
    else:
        print('human rights')

def main_12():
    s = filter()
    words = get_words()
    for i in s:
        if words.find(i) > -1:
            words = words.replace(i, '***')
    print(words)
    
if __name__ == '__main__':
    main_11()
    # main_12()