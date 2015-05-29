#!/usr/bin/env python
import sys, os,StringIO,csv
for line in sys.stdin:
	line=line.replace('\t',',')
	csv_file = StringIO.StringIO(line)
	csv_reader = csv.reader(csv_file)
	for words in csv_reader:
		if len(words)==16:
			filename='license'
		else:
			filename='table'
		key=words[0]
		value=words[1:]
		
		if key!='medallion':
			print key+'^'+filename+'^'+'|'.join(value)