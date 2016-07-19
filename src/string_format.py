#!/usr/bin/python

num = int(raw_input())
width = len('{0:b}'.format(num))
for i in range(1,num+1):
	
	for base in 'doXb':
		print '{0:{width}{base}}'.format(i,width=width,base=base),
	print 
