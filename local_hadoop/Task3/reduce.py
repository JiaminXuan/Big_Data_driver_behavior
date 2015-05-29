#!/usr/bin/python

import sys

current_word = None
current_sum = 0
dict = {}

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    word, count = line.strip().split("\t", 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if word == current_word:
        current_sum += count
    else:
        if current_word:
            # output goes to STDOUT (stream data that the program writes)
            dict[current_word] = current_sum #print "%s\t%d" %( current_word, current_sum )
        current_word = word
        current_sum = count
dict[current_word] = current_sum
cout = 0
for item in sorted(dict.items(), key = lambda x: -x[1]):
        if cout < 100:
                print "%s\t%d" %( item[0], item[1] )
                cout += 1
        else:
                break

