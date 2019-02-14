# 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 （http://tieba.baidu.com/p/2166231880?see_lz=1）
# coding:UTF-8

import urllib, re
import urllib.request

# 构建headers 头
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}

def get_img_url(page_url):
    # 发送请求
    request = urllib.request.Request(page_url, headers=headers)
    # 获取返回数据
    response = urllib.request.urlopen(request)
    # 读取网页
    page = response.read().decode('utf-8')
    # print(page)
    # 获取每条 <img>标签
    regex = re.compile('<img.+?class="BDE_Image".+?>')
    img_list = regex.findall(page)
    # print(img_list)
    return img_list

def dowm_img(url_list, path):
    counter = 1
    # 获取图片链接
    r = re.compile('http.+?.jpg?')
    for url in url_list:
        url = r.findall(url)
        # 下载
        urllib.request.urlretrieve(url[0], path+'\\'+str(counter)+'.jpg')
        counter += 1
    # print('done')
    # print(url_list)

def main():
    path = r'C:\Users\pp\Pictures\妹子\新垣结衣'
    # url = r'http://tieba.baidu.com/p/2166231880?see_lz=1'
    url = r'http://tieba.baidu.com/p/5596022626?see_lz=1'
    url_list = get_img_url(url)
    dowm_img(url_list, path)

if __name__ == '__main__':
    main()