#!/usr/bin/env python
import sys, os
for line in sys.stdin:
    line=line.strip()
    words=line.split(',')
    if words[0]=='medallion':
        pass
    else:
        if len(words)<12:
            filename='fares'
            key=','.join(words[:4])
            value=','.join(words[4:])
        else:
            filename='trips'
            keys=[words[i] for i in [0,1,2,5]]
            key=','.join(keys)
            values=[words[i] for i in range(len(words)) if i not in [0,1,2,5]]
            value=','.join(values)
        print '%s^%s^%s'%(key,filename,value)
    