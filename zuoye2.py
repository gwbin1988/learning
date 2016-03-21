# -*- coding: utf-8 -*-
#二分查找插入排序
arr=[3,4,1,2,0,10,9,100,89,67,99,1001,55]
length=len(arr)
count=0
for i in range(1,length):
    key=arr[i]
    low=0
    high=i-1
    count=count+1
    while(low<=high):
        middle=(low+high)/2
        if arr[middle]>key:
            high=middle-1
        else:
            low=middle+1
    for j in range(low,i)[::-1]:
        arr[j+1]=arr[j]
    arr[low]=key
print arr
print count
