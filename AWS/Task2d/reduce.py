#!/usr/bin/env python

from operator import itemgetter
import sys,string
import numpy as np
current_time=None
current_list=[]
for line in sys.stdin:
    line = line.strip()
    time,revenue=line.split('^')
    revenue=revenue.split(',')
    try:
        revenue=map(float,revenue)
    except:
        pass

    if current_time == time:
        current_list=np.array(current_list)
        revenue=np.array(revenue)
        current_list+=revenue
    else:
        if current_time:
            print '%s\t%.2f,%.2f,%.2f,%.2f'%(current_time,current_list[0],current_list[1],current_list[2],current_list[3])
        current_list = revenue
        current_time = time
# do not forget to output the last word if needed!
if current_time == time:
    print '%s\t%.2f,%.2f,%.2f,%.2f'%(current_time,current_list[0],current_list[1],current_list[2],current_list[3])