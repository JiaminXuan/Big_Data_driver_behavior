#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    key,value = line.split('\t')
    value=value.split(',')
    print '%s\t%s' % (value[11], 1)