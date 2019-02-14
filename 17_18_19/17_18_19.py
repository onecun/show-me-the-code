# xls 转 xml
# coding: UTF-8
# 使用 xrld 模块操作 xls文件
# 使用 xml.dom.minidom 模块操作 xml 文件

import xlrd
import xml.dom.minidom as md

# # 用于 17题和18题
def get_xlscontent(path):
    # 打开工作簿
    workbook = xlrd.open_workbook(path)
    # 打开表
    sheet = workbook.sheets()[0]
    # print(sheet.nrows)
    # 获取表里的内容
    content = {}
    for i in range(sheet.nrows):
        content[i+1] = sheet.row_values(i)[1:]
    return content

# 用于 19题，语法基本同上 
def get_xlscontent_19(path):
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheets()[0]
    content = []
    for i in range(sheet.nrows):
        content.append(sheet.row_values(i))
    return content

# 将内容写入xml
def wirte_xml(content):
    # 获取一个xml文档
    doc = md.Document()
    # 创建一个root标签
    root = doc.createElement('root')
    # 将root添加进xml文档
    doc.appendChild(root)
    # 用循环添加多个p标签及内容
    for i in range(len(content)):
        # 创建p标签
        p = doc.createElement('p')
        root.appendChild(p)
        # 创建一个 文本节点
        xmlcontent = doc.createTextNode(str(content[i]))
        # 将 文本节点 添加到 p标签
        p.appendChild(xmlcontent)
    return doc

def save_xml(doc):
    # print(doc.toprettyxml(encoding='utf-8'))
    with open('17_18_19.xml', 'wb') as f:
        f.write(doc.toprettyxml(encoding = 'utf-8'))

def main():
    path = [
    r'C:\Users\pp\Documents\Python\show_my_code\14_15_16\student.xls',
    r'C:\Users\pp\Documents\Python\show_my_code\14_15_16\city.xls',
    r'C:\Users\pp\Documents\Python\show_my_code\14_15_16\num.xls'
    ]
    # 将17，18题 与 19题分开操作
    content = []
    for i in range(len(path)):
        if i < 2:
            c = get_xlscontent(path[i])
        else:
            c = get_xlscontent_19(path[i])
        content.append(c)
    doc = wirte_xml(content)
    save_xml(doc)

if __name__ == '__main__':
    main()