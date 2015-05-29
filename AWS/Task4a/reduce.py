#!/usr/bin/env python

from operator import itemgetter
import sys

current_cartype = None
current_count = 0
current_amount=0.0
current_tips=0.0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    cartype,count,totalamount,tips = line.strip().split('^')
    # convert count (currently a string) to int
    try:
        count = int(count)
        totalamount=float(totalamount)
        tips=float(tips)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_cartype== cartype:
        current_count += count
        current_amount+=totalamount
        current_tips+=tips
    else:
        if current_cartype:
            # write result to STDOUT
            try:
                tips_p=current_tips/current_amount*100
            except:
                tips_p=0
            print "%s,%s,%.2f,%.2f"%(current_cartype,current_count,current_amount,tips_p)
        current_count = count
        current_cartype= cartype
        current_amount=totalamount
        current_tips=tips


# do not forget to output the last word if needed!
if current_cartype== cartype:
    try:
        tips_p=current_tips/current_amount*100
    except:
        tips_p=0
    print "%s,%s,%.2f,%.2f"%(current_cartype,current_count,current_amount,tips_p)