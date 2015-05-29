#!/usr/bin/env python

from operator import itemgetter
import sys
current_count=0
for line in sys.stdin:
    line = line.strip()
    try:
        count = int(line)
    except ValueError:
        continue
    current_count+=count
print current_count