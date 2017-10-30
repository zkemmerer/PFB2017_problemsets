#!/usr/bin/env python3

import sys

blast_one = open('blast_rand5-200_v_qfo_BLOSUM62.txt', 'r')

#blast_file = open(sys.argv[1])
#matrix = sys.argv[2]
#print (sys.argv[1] + sys.argv[2])

blast_dict = {}
fields = ''
line =''
for line in blast_one:
    if not line.startswith('#'):
        line = line.rstrip()
        line = line.split('\t')
        blast_dict [fields] = line
    elif line.startswith('#Field'):
        line  = line.rstrip()
        fields  = line.split('\t')
        blast_dict [fields] = line
print (blast_dict) 
