# -*- coding: utf-8 -*-

arr=[1,2,3,6,123,345,-2,-8]

swap=arr[0]
length=len(arr)
while length>0:
    for n in range(length-1):
        if arr[n]>arr[n+1]:
            swap=arr[n]
            arr[n]=arr[n+1]
            arr[n+1]=swap
    length-=1
print arr



len_of=0

max_num=0

min_num=0

for n in arr:
    len_of+=1
print len_of

for n in arr:
    if n>max_num:
        max_num=n
print max_num

for n in arr:
    if n<min_num:
        min_num=n
print min_num

string_arr=['c','python','js','css','html','node']
string_arr[0]='java'
print string_arr

string_arr[-1]='ruby'
print string_arr

list_str=[]
flag=True
while flag:
  str=raw_input("please enter the command:")
  if str=="add":
         input_str=raw_input("please enter the string:")
         list_str.append(input_str)
         print list_str
  elif str=="do":
      print list_str.pop(0)
      if len(list_str)==0:
           print "nothing to do"
           break


