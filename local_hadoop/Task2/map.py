#!/usr/bin/python

import sys
import csv
import string 

f = open("stop-word-list.csv")
reader = csv.reader(f) 
onestop = reader.next()
stopList = []

for word in onestop:
	stopList.append(word.strip()) 

exclude=set(string.punctuation+string.digits)


def firstLetter(word):
    initialLetter = word[0]
	letter = initialLetter.upper()
	return "%s\t%d" %(letter, 1)

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    l = line.strip().split()
    
    for word in l:	
	updatedWord = word.translate(None, exclude+ " ")
 
	if len(updatedWord) == 0 or updatedWord in stopList: 
		pass
	else:
		print firstLetter(updatedWord) 	
        	

