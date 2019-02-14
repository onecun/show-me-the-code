# json 转 excle
# coding: UTF-8
# 
# ''' 14题
# {
# 	"1":["张三",150,120,100],
# 	"2":["李四",90,99,95],
# 	"3":["王五",60,66,68]
# }
# '''
# 
# ''' 15题
# {
#     "1" : "上海",
#     "2" : "北京",
#     "3" : "成都"
# }
# '''
# ''' 16题
# [
# 	[1, 82, 65535], 
# 	[20, 90, 13],
# 	[26, 809, 1024]
# ]
# '''

import xlwt
import json

def get_dict(path):
    with open(path, 'r', encoding='utf-8') as file:
        f = file.read()
    # json.loads() 方法反序列化json格式文件
    d = json.loads(f)
    # print(d)
    return d

def write_xls_14(d):
    # 创建新的xls文件
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建新的表
    worksheet = workbook.add_sheet('student')
    row, col = 0, 0
    # print(d)
    # 用循环写入每行的数据
    for k in d:
        worksheet.write(row, col, k)
        for j in range(len(d[k])):
            col = col + 1
            # 参数对应 行，列， 值。从0开始
            worksheet.write(row, col, d[k][j])
        row += 1 
        col = 0
    workbook.save('student.xls')

def write_xls_15(d):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('student')
    row, col = 0, 0
    for k in d:
        worksheet.write(row, col, k)
        worksheet.write(row, col+1, d[k])
        row += 1
        col = 0
    workbook.save('city.xls')

def write_xls_16(l):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('student')
    row, col = 0, 0
    for i in l:
        for j in range(len(i)):
            worksheet.write(row, col, i[j])
            col += 1
        row += 1
        col = 0
    workbook.save('num.xls')
            
            

if __name__ == '__main__':
    write_xls_14(get_dict('14.txt'))
    write_xls_15(get_dict('15.txt'))
    write_xls_16(get_dict('16.txt'))

    
