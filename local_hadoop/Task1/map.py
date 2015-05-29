#!/usr/bin/python

import sys
import csv
import string 
# load stop words into  list
f = open("stop-word-list.csv")
reader = csv.reader(f) 
justoneline = next(reader)
stopList = []

for word in justoneline:
	stopList.append(word.strip()) 
# load punctuation and digits
exclude=set(string.punctuation+string.digits)
# process each line in stdin and 
for line in sys.stdin:
	l = line.strip().split()
    
   	for word in l:	
	
		updatedWord = word.translate(None, exclude)
       
		if len(updatedWord) == 0 or updatedWord in stopList:
			pass
		else:
       		print "%s\t%d" %(updatedWord, 1)  
	
        	

