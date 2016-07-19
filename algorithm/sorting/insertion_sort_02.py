#!/bin/python
def insertionSort(ar):  
    print " ".join(str(num) for num in ar)
    print "-----------------------------------"
    for i in range(1,len(ar)):
        curVal = ar[i]
        position = i
        
        
        while position>0 and ar[position-1]>curVal:
            ar[position] = ar[position-1]
            
            position = position-1
            
        ar[position] = curVal
        print i," ".join(str(num) for num in ar)
        
   
    

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)