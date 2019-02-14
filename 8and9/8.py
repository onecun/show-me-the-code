#  一个HTML文件，找出里面的正文和链接。
# coding:utf-8

from bs4 import BeautifulSoup
import requests
f = open('a.html', 'r', encoding = 'UTF-8')
soup = BeautifulSoup(f.read(),'lxml')
# print(soup.prettify())
# print(soup.text)
articals = soup.find_all('p')
for a in articals:
    print(a)

urls = soup.find_all('a')
for u in urls:
    print(u['href'])

f.close()