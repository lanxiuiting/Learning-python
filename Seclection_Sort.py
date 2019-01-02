# -*- coding: UTF-8 -*-
def findSmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index
def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest=findSmallest(arr)
        newArr.append(arr.pop(smallest))#pop的作用是去掉每次出来最小的那个数#
    return newArr
print selectionSort([5,4,6,9,8,1])
