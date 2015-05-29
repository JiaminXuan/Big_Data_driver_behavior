#!/usr/bin/env python
import sys, os,StringIO,csv
a={}
for line in sys.stdin:
    words=line.strip().split('\t')
    key=words[0]
    value=words[1].split('|')
    try:
        totalamount=float(value[14])+float(value[15])+float(value[17])+float(value[18])
        agencyname=value[29]
        if agencyname in a:
            a[agencyname]+=totalamount
        else:
            a[agencyname]=totalamount
    except:
        pass
for agencyname in a:
    print '%s^%.2f'%(agencyname,a[agencyname])