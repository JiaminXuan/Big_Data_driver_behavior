#!/usr/bin/env python
import sys, os,StringIO,csv
a=0
b=0
for line in sys.stdin:
    words=line.strip().split('\t')
    key=words[0]
    value=words[1].split('|')
    try:
        cartype=value[25]
        totalamount=float(value[14])+float(value[15])+float(value[17])+float(value[18])
        tips=float(value[17])
        print "%s^%s^%s^%s"%(cartype,1,totalamount,tips)
    except:
        pass