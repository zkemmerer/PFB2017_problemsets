#!/usr/bin/env python3

import re
nobody = open('Python_06_nobody.txt', 'r')
pattern = 'Nobody'
len (re.findall(pattern, nobody))
print (len)
