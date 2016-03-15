#!/usr/bin/python
import string

size = int(raw_input())
alphabet = string.ascii_lowercase

for i in range(size - 1, 0, -1):
	row = ["-"] * (size * 2 - 1)
	print '-----------------------------1----------------------------------',row
	
	for j in range(0, size - i):
		row[size - 1 - j] = alphabet[j + i]
		print '-----Row--2---',row
		row[size - 1 + j] = alphabet[j + i]
		print '-----Row--3---',row
	print("-".join(row))
