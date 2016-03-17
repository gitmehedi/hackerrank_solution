#!/usr/bin/python
textInput = int(raw_input())
text = raw_input()
width = textInput+textInput-1

for i in range(textInput):
	s = (i*2)*text+text
	print s.center(width,' ')
	
for i in range(textInput):
	s = textInput*text
	print s.center(textInput*2)+s.center(textInput*6)
	
for i in range(textInput):
	s = textInput*textInput*text 
	print s.center(textInput*6)

for i in range(textInput):
	s = textInput*text
	print s.center(textInput*2)+s.center(textInput*6)

for i in range(textInput-1,-1,-1):
	s = (i*2)*text+text
	print ''.center(textInput*4-1,' '),s.center(width,' ')


"""
thickness = int(raw_input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)

#Top Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)

#Middle Belt
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)    

#Bottom Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)    

#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6) 
"""

	
