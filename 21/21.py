# 密码加密
# coding: UTF-8
# 使用hash算法加密，（md5.sh1 等常用算法）
import hashlib

user = input('用户名：')
password = input('密码：')
md5_password = user+password
# 
md5 = hashlib.md5()
# 将密码添加进 md5算法中(在字符串过长时，可以用多个update)
md5.update(md5_password.encode('utf-8'))

print('加密密码：'+md5.hexdigest())