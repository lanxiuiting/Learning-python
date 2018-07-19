#e4.3TextProgressBar.py
import time
scale=50
print("执行开始".center(25,'-'))
t=time.clock()
for i in range(scale+1):
   a='*'*i
   b='.'*(scale-i)
   c=(i/scale)*100
   t-=time.clock()
   print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,-t),end='')
   time.sleep(0.05)
print("执行结果".center(25,'-'))
#{:^3.0f}格式化百分比
