#!/usr/bin/env python3

import sys, os

# kmer_length fastq_filename num_top_report

usage = '\n\n\tusage: () kmer_length fastq_filename num_top_report\n\n\n'.format(sys.argv[0])

if len(sys.argv) < 4:
   sys.stderr.write(usage)
   sys.exit(1)

kmer_length = int(sys.argv[1])
fastq_filename = sys.argv[2]
num_top_kmer = int(sys.argv[3])

kmer_dict = {}

def count_kmers(kmer_dict, sequence, kmer_length):
    for window_start in range(0, len(sequence) - kmer_length + 1):
       kmer = sequence[window_start:window_start + kmer_length]
       if kmer in kmer_dict:
          kmer_dict[kmer] += 1
       else:
          kmer_dict[kmer] = 1
 
##ready to work

fh = open('/Users/admin/problemsets/PFB2017_repository/reads.fq', 'r')
line_counter = 0
for line in fh:
    line_counter += 1
    line = line.rstrip()

    if line_counter % 4 == 2:
     	# sequence record
       sequence = line
       count_kmers(kmer_dict, sequence, kmer_length)

#sort
sorted_kmers = sorted(kmer_dict, key=lambda x:kmer_dict[x], reverse=True)

sorted_kmers = sorted_kmers[0:num_top_kmer]

for kmer in sorted_kmers:
    count = kmer_dict[kmer]
    print('{}\t\{}'.format(kmer,count))

# this is totally unsorted:
#for (kmer, count) in kmer_dict.items():
#    print('{}\t\{}'.format(kmer, count))

sys.exit(0)
#this is good practice, can help ID problem in pipeline
