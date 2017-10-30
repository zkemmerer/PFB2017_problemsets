#!/usr/bin/env python3

import Bio

from Bio import SeqIO
fasta = open('uniprot_sprot.fasta')

record =''
count = 0
for record in SeqIO.parse(fasta, 'fasta'):
    record = record.split('\n')
    print (record)
