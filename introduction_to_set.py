#!/usr/bin/python
"""
This method takes argument like this 
i=3
b
----
12
23
12
"""
i = int(raw_input())
b = set([float(raw_input()) for k in range(i) ])
print sum(b)/len(b)

print "-------------for second list------------------"
"""
This method takes argument like this 
i=3
b = '12 23 12'
"""
i = int(raw_input())
b = set(map(float,raw_input().split()))
print sum(b)/len(b)
