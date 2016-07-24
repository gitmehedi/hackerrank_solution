#!/bin/bash

V = int(raw_input("Search Number: "))
n = int(raw_input("Array Length: "))
arr = [int(x) for x in raw_input().split()]

for ind,i in enumerate(arr):
    if(V==i):
        print "Index no of the search number: ", ind