#CalStatistics.py
from math import sqrt
def getNum():
    nums=[]
    iNumstr=input("请输入数字（直接输入回车退出）:")
    while iNumstr !="":
        nums.append(eval(iNumstr))
        iNumstr=input("请输入数字（直接输入回车退出）:")
    return nums
def Max(numbers):
    Max=max(numbers)
    return Max
def Min(numbers):
    Min=min(numbers)
    return Min
n=getNum()
print("最大值:{}，最小值:{}.".format (Max(n),Min(n)))
