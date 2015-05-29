#!/usr/bin/env python
import sys
for line in sys.stdin:
	line = line.strip()
	key,value = line.split('\t')
	value=value.split(',')
	total=value[3]
	print '%s\t%s' % (total, 1)
