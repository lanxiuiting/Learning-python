def binary_search(list,item):
    low=0
    high=len(list)-1
    while low<=high:
        mid =(low+high)/2
        guess=list[mid]
        if guess==item:
            return mid
        if guess>item:
            high=mid-1
    else:
        low=mid-1
    return None
#使用键盘输入#
print"type your list throught the keyboard:"
a=raw_input(">")
x=a.split(" ")
y=[int(a[i])for i in range(len(a))]
print "type the number you want to search:"
item=int(raw_input(">"))
print binary_search(y,item)
