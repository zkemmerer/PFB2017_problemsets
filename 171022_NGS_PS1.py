#!/usr/bin/env python3

fastq = open('pfb.fastq.2', 'r') 

gene =[]
line_count = 0
for line in fastq:
    if (line % 4 == 2):
        #print (len(line))
        gene.append(line)
print (gene)


