#!/usr/bin/env python3

import sys, os
import re


#fastq_dict ={}
sequence = ''
quality = ''

line_counter = 0
fastq_file = open ('Python_05.fastq', 'r')
for line in enumerate(fastq_file):
#    line_counter += 1

    if line % 4 == 2:
        line = line.rstrip() 
        sequence = line
        fasta_dict[sequence] = score
    elif line_counter % 4 == 0:
        score = line
        fastq_dict[sequence] = score
print (fastq_dict)

#for score in fastq_dict:
#    score_cv = [(ord(base)-33) for base in score]
#    print (score_cv)

