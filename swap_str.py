#!/usr/bin/python
str = raw_input()
nStr = '2'
print "ffffffffffffffffff"
for i in range(len(str)):
    if str[i].islower():
        nStr += str[i].upper()
    elif str[i].isupper():
        nStr += str[i].lower()
    else:
        nStr += str[i]

        
print nStr
