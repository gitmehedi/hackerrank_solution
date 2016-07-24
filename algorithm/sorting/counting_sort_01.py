#!/bin/bash

def countSort(arr):
    outArr = [0 for x in range(9)]
    cArr = [0 for x in range(9)]
    ansArr = ['' for x in arr]
    
    for i in range(9):
        cArr[i] +=1
    
    for i in range(9):
        cArr[i] = cArr[i-1]
        
    for i in range(len(arr)):
        outArr[cArr[i]-1] = arr[i]
        cArr[i] -=1
        
    for i in range(len(arr)):
        ansArr[i] = outArr[i]
    
    return ans
    
    
n = int(raw_input())
x = [int() for x in range(n)]
countSort(x)

for i in x:
    print x
