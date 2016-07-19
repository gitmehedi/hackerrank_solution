#!/usr/bin/python

str = raw_input()
pos,key = raw_input().split()
string = str[:int(pos)]+key+str[int(pos)+1:]

print string
