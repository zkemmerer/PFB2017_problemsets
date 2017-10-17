#!/usr/bin/env python3
import sys
count = float(sys.argv[1])
if count < 0:
	message = "is less than 10"
	print (count, message)
elif count > 0:
	message = "is greater than 10"
	print (count, message)
else:
	message = "not true"
	print (message)
