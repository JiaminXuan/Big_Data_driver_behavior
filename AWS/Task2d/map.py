#!/usr/bin/env python
import sys,string
for line in sys.stdin:
	line = line.strip()
	key,value = line.split('\t')
	key=key.split(',')
	value=value.split(',')
	time=key[3][:10]
	fares=[value[i] for i in [-6,-5,-3,-2]]
	revenue=','.join(fares)
	print '%s^%s'%(time,revenue)
