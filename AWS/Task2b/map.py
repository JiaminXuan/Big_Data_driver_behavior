#!/usr/bin/env python
import sys
count=0
for line in sys.stdin:
	line = line.strip()
	key,value = line.split('\t')
	value=value.split(',')
	total=float(value[-1])
	if total<=10:
		count+=1
print count
