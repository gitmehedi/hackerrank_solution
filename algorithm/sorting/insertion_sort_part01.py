#!/bin/python

# def insertionSort(list):
#     for index in range(1,len(list)):
#         on_deck = list[index]
#         comparing = index - 1
# 
#         while comparing >= 0 and on_deck < list[comparing] :
#             list[comparing+1] = list[comparing]
#             print ' '.join(str(num) for num in list)
#             list[comparing] = on_deck
#             comparing -= 1
# 
#     print ' '.join(str(num) for num in list)
#     
# # Tail starts here
# 
# m = input()
# ar = [int(i) for i in raw_input().strip().split()]
# insertionSort(ar)

def insertionSort(ar):    
     
    for index in range(1,len(ar)):
        curVal = ar[index]
        position = index
         
        while position>0 and ar[position-1]>curVal:
            ar[position]=ar[position-1]
            print ' '.join(str(num) for num in ar)
            position = position - 1
             
        ar[position]=curVal
         
    print ' '.join(str(num) for num in ar)
          
m = raw_input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

# def insertionSort(alist):
#    for index in range(1,len(alist)):
# 
#      currentvalue = alist[index]
#      position = index
# 
#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1
# 
#      alist[position]=currentvalue
# 
# alist = [54,26,93,17,77,31,44,55,20]
# insertionSort(alist)
# print(alist)