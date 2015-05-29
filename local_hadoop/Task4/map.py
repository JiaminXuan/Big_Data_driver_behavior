#!/usr/bin/python

import sys
import csv
import string 
import os

f = open("stop-word-list.csv")
reader = csv.reader(f) 
onestop = reader.next()
stopList = []

for word in onestop:
	stopList.append(word.strip()) 

exclude=set(string.punctuation+string.digits)
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	
	env = os.environ['mapreduce_map_input_file'][-4:]
	#env = int(env)
	#env = os.environ['HOME']

	l = line.strip().split()
    
   	for word in l:	
	
		updatedWord = word.translate(None, exclude)
       
		if len(updatedWord) == 0 or updatedWord in stopList:
			pass
		else:
			g = (env, 1)  
       				#print "%s\t(%d, %d)" % (updatedWord, env, 1)  
			print "%s\t%s" % (updatedWord, g) 
        	

