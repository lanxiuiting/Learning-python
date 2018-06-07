# exchange rate.py
value = input("请输入带货币表示符号的金钱数(例如: 32R): ")
if value[-1] in ['R','r']:
    F= 6*eval(value[0:-1])
    print("转换后的金钱数量为: {:.0f}D".format(F))
elif value[-1] in ['D','d']:
    C= eval(value[0:-1])/6
    print("转换后的温度为: {:0f}R".format(C))
else:
    print("输入有误")
