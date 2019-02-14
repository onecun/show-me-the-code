# -*- coding:utf-8 -*-

import mysql.connector

def connectDb():
    #连接到mysql
    db = mysql.connector.connect(user='root', password='123456', database='test', use_unicode=True)
    return db

def createTable(cursor):
    #删除表 1pykeys
    cursor.execute('DROP TABLE 1pykeys')
    #创建新的表
    sql = """CREATE TABLE 1pykeys (
        id int NOT NULL AUTO_INCREMENT,
        code varchar(20),
        PRIMARY KEY (id)
    )"""
    cursor.execute(sql)

def writeDb(cursor):
    f = open('keys.txt', 'r')
    for line in f.readlines(): #一行行的读取
        coupon = line.strip() #用strip()去掉每行的'\n'
        #插入数据， mysql只接受list,所以在使用[coupon]
        cursor.execute("INSERT INTO 1pykeys(code) VALUES (%s)", [coupon])
    f.close()

#提交数据，关闭游标和数据库
def closeDb(db, cursor):
    db.commit()
    cursor.close()
    db.close()

def main():
    db = connectDb() #获取数据库
    cursor = db.cursor() #获取游标
    createTable(cursor)
    writeDb(cursor)
    closeDb(db, cursor)

if __name__ == '__main__':
    main()
