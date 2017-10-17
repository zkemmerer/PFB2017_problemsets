#!/usr/bin/env python3
import sys
count = float(sys.argv[1])
if count > 0:
	message = "is greater than 0"
	print (count, message)
	if count < 50:
		message = "is less than 50"
		print (count, message)
		if count %2 == 0:
			message = "is even"
			print (count, message)
	elif count > 50:
		message = "is greater than 50"
		print (count, message)
		if count %3 == 0: 
			message = "is divisible by 3"
			print (count, message)
