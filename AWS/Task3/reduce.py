#!/usr/bin/env python

from operator import itemgetter
import sys,string

current_key = None
storage_table=[]
storage_license=[]

for line in sys.stdin:
	key,filename,value = line.strip().split('^')
	if key==current_key:
		if filename=='table':
			storage_table.append(value)
		else:
			storage_license.append(value)
		# print ('add one value to existing storage')
	else:
		try:
			for i in storage_license:
				for j in storage_table:
					output=j+'|'+i
					print current_key.strip()+'\t'+output

					# print output
		except: 
			pass
			# print('the first one---None---skip')
		storage_table[:]=[]
		storage_license[:]=[]
		current_key=key
		# print ('clear storage')
		if filename=='table':
			storage_table.append(value)
		else:
			storage_license.append(value)
		# print ('initiate one storage')
try:
	for i in storage_license:
		for j in storage_table:
			output=j+'|'+i
			print current_key.strip()+'\t'+output

			# print output
except: 
	pass