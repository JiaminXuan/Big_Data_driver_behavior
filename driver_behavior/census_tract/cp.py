#!/usr/bin/env python
import os,sys
a="https://s3.amazonaws.com/nyu-big-data-ajax/newdatasettrip2011"
for m in [5]:
	for i in range(8):
		print '%s_%s/part-0000%d-2011-%s'%(a,m,i,m)
		# os.system('wget %s_%s/part-0000%d'%(a,m,i))
		# os.system('cat part-000*>%s;rm part-000*'%(m))
	# print '%s%02d'%(a,i)
