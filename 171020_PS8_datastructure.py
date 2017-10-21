#!/usr/bin/env python3

#make dict from fasta file
fasta = open ('Python_08.fasta', 'r')
sequence = ''
genes = {}
for line in fasta:
    line = line.strip()
    if line.startswith('>'):
            header = line 
            genes[header] = sequence
    else:
        sequence = line.rstrip('\n')
        genes[header] += sequence #additional seq added to dict
print(genes)

nt_comp = {}
nt = ''
comp = ''
dna = []
dna.append(dnaA,dnaT,dnaG,dnaC)
for nt in dna:
    line = line.strip()
            header = line
            nt_comp[header] = nt
    else:
        sequence = line.rstrip('\n')
        genes[header] += sequence #additional seq added to dict
print(genes)

nt = ''
comp = ''
dnaA = '{:.1%}'.format(sequence.count('A')/len(sequence))
dnaT = '{:.1%}'.format(sequence.count('T')/len(sequence))
dnaG = '{:.1%}'.format(sequence.count('G')/len(sequence))
dnaC = '{:.1%}'.format(sequence.count('C')/len(sequence))
#nt_comp = {'A':dnaA, 'T':dnaT, 'G':dnaG, 'C':dnaC}


#for nt, comp in nt_comp:
   # for header in genes:
       # genes [header][nt] = comp
#print (genes)
