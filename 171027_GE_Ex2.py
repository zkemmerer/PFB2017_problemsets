#!/usr/bin/env python3

import os, sys, re

myDict = {}

fh = open('bowtie2.sam')
for line in fh:
    line = line.rstrip()
    fields = line.split('\t')

    read_name = fields[0]
    combo_name = fields[2]

    (gene_id, transcript_id) = combo_name.split('^')

    if gene_id not in myDict:
        myDict[gene_id] = set()

    myDict[gene_id].add(read_name)

gene_ids = sorted(myDict, key=lambda x: len(myDict[x]), reverse=True)

for gene_id in gene_ids:
    mySet = myDict[gene_id]
    num_reads = len(mySet)

    print ('{}\t{}'.format (gene_id, num_reads))

sys.end(0)


