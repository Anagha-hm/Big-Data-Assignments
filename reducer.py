#!/usr/bin/env python3

import datetime
import sys 

output = {}

for line in sys.stdin:
	#line = line.strip()		
	
	'''hour = line['Start_time'].datetime.hour
	if hour not in output.keys():
		output[hour] = 1
	else:
		output[hour] = output[hour] + 1''' 
		
	print(line)
	
	
	
