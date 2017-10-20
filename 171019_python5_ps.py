#!/usr/bin/env python3

python_uppercase = open('pfb2017/files/Python_05.txt', 'r')
python_read = python_uppercase.read()
python_upper = python_read.upper()
print ('python_upper')
#Open, read and capitalize txt file

python_uppercase = open('pfb2017/files/Python_05.txt', 'r')
python_read = python_uppercase.read()
python_upper = python_read.upper()
python_write = open('Python_05_uc.txt', 'w')
python_write.write(str(python_upper))
python_write.close ()
print ("wrote to file 'Python_05_uc.txt'")
#Write to previous txt file to new file

fasta = open('Python_05.fasta', 'r')
reverse = fasta.read()


#fasta_dict['seq1'] = 'AAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGCCACCAATTATGGTGTATGAGTGAATCTCTGGTCCGAGATTCACTGAGTAACTGCTGTACACAGTAGTAACACGTGGAGATCCCATAAGCTTCACGTGTGGTCCAATAAAACACTCCGTTGGTCAAC'
#fasta_dict['seq2'] = 'GCCACAGAGCCTAGGACCCCAACCTAACCTAACCTAACCTAACCTACAGTTTGATCTTAACCATGAGGCTGAGAAGCGATGTCCTGACCGGCCTGTCCTAACCGCCCTGACCTAACCGGCTTGACCTAACCGCCCTGACCTAACCAGGCTAACCTAACCAAACCGTGAAAAAAGGAATCT'
#fasta_dict['seq3'] = 'ATGAAAGTTACATAAAGACTATTCGATGCATAAATAGTTCAGTTTTGAAAACTTACATTTTGTTAAAGTCAGGTACTTGTGTATAATATCAACTAAAT'
#fasta_dict['seq4'] ='ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAAACAACATGCCAAATAGAAACGATCAATTCGGCGATGGAAATCAGAACAACGATCAGTTTGGAAATCAAAATAGAAATAACGGGAACGATCAGTTTAATAACATGATGCAGAATAAAGGGAATAATCAATTTAATCCAGGTAATCAGAACAGAGGT'

sequence = ''
header = ''
for line in fasta:
    if line.startswith('>'):
        if sequence != '':
            print (header, sequence)
            header = line
            sequence = ''
        else:
            header = line
    if not line.startswith('>'):
        sequence += line.rstrip('\n')
print(header, sequence)        
