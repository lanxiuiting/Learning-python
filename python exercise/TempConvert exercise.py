# TempConvert.py
value = input("请输入带温度表示符号的温度值(例如: 32C): ")
if value[-1] in ['C','c']:
    F= 1.8 *eval(value[0:-1])+ 32
    print("转换后的温度为: {:.0f}F".format(F))
elif value[-1] in ['F','f']:
    C= (eval(value[0:-1]) - 32) / 1.8
    print("转换后的温度为: {:0f}C".format(C))
else:
    print("输入有误")
