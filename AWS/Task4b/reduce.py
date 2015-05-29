#!/usr/bin/env python
a={}
from operator import itemgetter
import sys
for line in sys.stdin:
    agencyname,totalamount = line.strip().split('^')
    try:
        totalamount=float(totalamount)
        if agencyname in a:
            a[agencyname]+=totalamount
        else:
            a[agencyname]=totalamount
    except:
        pass
sorted_a=sorted(a.items(),key=itemgetter(1),reverse=True)
for i in xrange(10):
    print '%s\t%.2f'%(sorted_a[i][0],sorted_a[i][1])