#!/usr/bin/env python

from operator import itemgetter
import sys,string

current_key = None
storage_trip=[]
storage_fare=[]

for line in sys.stdin:
    key,filename,value = line.strip().split('^')
    value=value.strip().split(',')
    if key==current_key:
        if filename=='trips':
            storage_trip.append(value)
        else:
            storage_fare.append(value)
        # print ('add one value to existing storage')
    else:
        try:
            for i in storage_fare:
                for j in storage_trip:
                    output=j+i
                    print current_key.strip()+'\t'+','.join(output)

                    # print output
        except: 
            pass
            # print('the first one---None---skip')
        storage_trip[:]=[]
        storage_fare[:]=[]
        current_key=key
        # print ('clear storage')
        if filename=='trips':
            storage_trip.append(value)
        else:
            storage_fare.append(value)
        # print ('initiate one storage')
try:
    for i in storage_fare:
        for j in storage_trip:
            output=j+i
            print current_key.strip()+'\t'+','.join(output)
            # print output
except: 
    pass