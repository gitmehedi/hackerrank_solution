#!/usr/bin/python
textInput = int(raw_input())
text = raw_input()
width = textInput+textInput-1

for i in range(textInput):
	s = (i*2)*text+text
	print s.center(width,' ')
	
for i in range(textInput):
	s = textInput*text
	print s.center(width,' '),s.center(width,' ')
	
for i in range(textInput):
	s = textInput*(textInput-1)*text+text 
	print s.center(width*3,' ')

for i in range(textInput):
	s = textInput*text
	print s.center(width,' '),s.center(width,' ')

for i in range(textInput-1,-1,-1):
	s = (i*2)*text+text
	print ''.center(width*2,' '),s.center(width,' ')

	
