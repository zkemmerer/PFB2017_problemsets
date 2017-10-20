#!/usr/bin/env python3

fasta = open('Python_05.fasta', 'r')
sequence = ''
header = ''
for line in fasta:
    if line.startswith('>'):
        if sequence != '':
            print (header, sequence, sep='')
            header = line
            sequence = ''
        else:
            header = line
    if not line.startswith('>'):
        sequence += line.rstrip('\n')
print(header, sequence, sep='')
