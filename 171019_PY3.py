#!/usr/bin/env python3

fasta = open('Python_05.fasta', 'r')
sequence = '' #empty string to store sequences/headers
header = '' 
gene_dict = {}
for line in fasta:
    line = line.strip() #strip lines at the beginning before loop
    if line.startswith('>'):
           # print (header, sequence.replace('A','t').replace('T','a').replace('G','c').replace\
#('C','g')[::-1], sep='')
            header = line #store header for dictionary/printing
            gene_dict[header] = sequence #appending headers into dictionary
    if not line.startswith('>'):
        sequence += line.rstrip('\n') #stitching sequence lines together
        gene_dict[header] = sequence #appending sequences into dictionary
#print(header, sequence.replace('A','t').replace('T','a').replace('G','c').replace\
#('C','g')[::-1], sep='')

print (gene_dict)
