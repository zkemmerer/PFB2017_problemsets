#!/usr/bin/env python3

import sys
from Bio import SeqIO

for record in SeqIO.parse('/Users/admin/problemsets/PFB2017_repository/reads.fq', 'fastq'):
    print (record.id + '\t' + record.seq)

kmer_length fastq_filename num


#script = sys.argv[0]
#reads = open(sys.argv[1])
#for line in sys.argv[2:]:
    #line.count % 4 == 2
#print (line)

