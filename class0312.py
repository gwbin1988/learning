# -*- coding: utf-8 -*-
# arr=list('hello')
#
# input_str='o'
# for s in arr:
#     if s==input_str:
#        input_str="True"
#        break
# print input_str
#
# num_list=range(10)
# max_num=0
# min_num=0
# length=0
# for s in num_list:
#     length+=1
# print length
#
# for n in num_list:
#     if n>max_num:
#         max_num=n
# print max_num
#
# for n in num_list:
#     if n<min_num:
#         min_num=n
# print min_num
#
# del arr[3]
# print arr
#
# print arr+num_list
# print arr*3
# arr[2]='w'
# print arr
# arr[-1]='0'
# print arr
#
# print num_list[1:]
# print num_list[:5]
# print num_list[-3:-1]
# print num_list[1:5:2]
# print num_list[5:1:-1]
# num_list[1:3]=''
# print num_list
# num_list[1:3]=list("hello")
# print num_list
# num_list.append(10)
# print num_list
#
# #追加 append
# #
# arr=list('hellow')
#
# total_num=0
# input_str='l'
# for s in arr:
#     if input_str in s:
#         total_num+=1
# print total_num
#
# arr=[1,8,4,3,9,10,100,80,23,45,21,2]
# length=len(arr)
# count=0
#
# while length>0:
#     for n in range(length-1):
#         count=count+1
#         if arr[n]>arr[n+1]:
#            arr[n],arr[n+1]=arr[n+1],arr[n]
#     length-=1
# print arr
#
#
# arr1=[1,8,4,3,9,10,100,80,23,45,21,2,100]
# print arr1.index(100)
# print arr1.index(100,arr1.index(100)+1)
# length=len(arr1)-1
# for j in range(length):
#     for i in range(length-j):
#         if arr1[i]>arr1[i+1]:
#             arr1[i],arr1[i+1]=arr1[i+1],arr1[i]
# print arr1
#
#
#
#
#
# arr_num=[1,2,3,4,5,6,7]
# arr_num.insert(3,'four')
#
# arr=[1,2,8,5,4]
# new_arr=[]
# print arr
#
# length=len(arr)
# for i  in range(length/2):
#     arr[i],arr[length-i-1]=arr[length-i-1],arr[i]
# print arr
#
# num_arr=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
#
#
# new_list2=[]
# for n in num_arr:
#     if n not in new_list2:
#        new_list2.append(n)
# print sorted(new_list2)
#
# def findsame(arr):
#     new_arr=[]
#     for n in arr:
#         if n not in new_arr:
#             new_arr.append(n)
#     print sorted(new_arr)
#
#
# arr1=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
# arr2=[2,1,3,2,43,234,454,452,234,14,21,14]
# print sorted(arr1)
# print sorted(arr2)
#
# new_list3=[]
# for n in arr1:
#     if n in arr2 and n not in new_list3:
#         new_list3.append(n)
# print new_list3
#
# #二分查找
# Num_list=range(100000)
# length=len(Num_list)
#
# Num=1111
# low=0
# high=length-1
# count=0
# while (low<=high):
#     count=count+1
#     middle=(low+high)/2
#     if Num_list[middle]>Num:
#          high=middle
#     elif Num_list[middle]<Num:
#          low=middle
#     else:
#          print middle,Num_list[middle]
#          break
#
# print count
#
# arr=[1,2,3,10,7,9,22,33,12]
# num=31
#
# num_dict={}
# for i in range(len(arr)):
#     need=num-arr[i]
#     x=arr[i]
#     if x in num_dict:
#          print i , arr[i]
#          print num_dict[x],arr[num_dict[x]]
#     else:
#          num_dict[need]=i
#
#
#
#
arr=list('python')
print arr

for o in ['we','pc','me','wd']:
    print o

print 'pc' in ['wd','pc']

# str=raw_input("please enter the string:")
# str_list=['pc','wd','st']
# for n in range(len(str_list)):
#     if str_list[n]==str:
#         print 'True',str

arr=['c','python','js','css','html','node']
del arr[2]
print arr

arr=['wd','pc']
print arr*2
arr1=['mw',1,2,3]
print arr+arr1

arr=['python','c','java','C++','js','node','html','css']
print arr[0]
print arr[-1]
print arr[-3]
print arr[1:3]
print arr[-3:-1]
print arr[:]
print arr[1:]
print arr[1:7:2]
print arr[::-2]
arr[2:4]=['pc','wd']
print arr
