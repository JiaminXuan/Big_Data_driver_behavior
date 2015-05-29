#!/usr/bin/env python
import sys,string
for line in sys.stdin:
	line = line.strip()
	key,value = line.split('\t')
	key=key.split(',')[0]
	print '%s^%s'%(key,1)
