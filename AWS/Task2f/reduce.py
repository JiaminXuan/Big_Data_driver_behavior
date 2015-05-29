#!/usr/bin/env python

from operator import itemgetter
import sys

current_driver = None
current_car = 0

for line in sys.stdin:
    line = line.strip()
    driver, car = line.split('^', 1)

    if driver == current_driver:
        if car != current_car:
            current_car +=1
    else:
        if current_driver:
            print driver+'\t'+str(current_car)
            current_car=0
            current_driver= driver
            current_car +=1
        current_driver= driver
        current_car +=1

