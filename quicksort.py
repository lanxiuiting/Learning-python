# -*- coding: utf-8 -*-
import xlrd
def quicksort(data):
    if len(data)<2:
        return data
    else:
        pivot=data[0]
        less=[i for i in data[1:] if i<=pivot]
        greater=[i for i in data[1:] if i>pivot]
        return quicksort(less)+[pivot]+quicksort(greater)
def read_excel():# 利用excel 读取文件#
    workbook=xlrd.open_workbook(r'C:\Users\lanxiuting\Desktop\data.xlsx')
    sheet1=workbook.sheet_by_index(0)
    data=sheet1.col_values(1)
    return data

print quicksort(read_excel())
          
