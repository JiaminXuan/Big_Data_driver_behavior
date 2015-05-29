#!/usr/bin/env python
import sys, os
for line in sys.stdin:
    line=line.strip()
    key,value=line.split('\t')
    key=key.split(',')
    value=value.split(',')
    print key[1]+'^'+key[0]