#!/usr/bin/env python3

import Bio

from Bio import SeqIO
fasta = open('uniprot_sprot.fasta') 

line_count = 0
for line in fasta:
    if line.startswith('>'):
        line_count += line.count('>')
        print (line_count)


