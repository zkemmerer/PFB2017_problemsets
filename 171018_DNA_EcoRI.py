#!/usr/bin/env python3

dna = """GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG"""
AT = (dna.count ('A') + dna.count ('T'))
GC = (dna.count ('G') + dna.count ('C'))
dna_length = len(dna)
AT_content = '{:.2%}'.format(AT/dna_length)
GC_content = '{:.2%}'.format(GC/dna_length)
#Determining the percentage of AT and GC in the sequence above

dna_compliment = dna.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
dna_reverse = str(dna_compliment)[::-1]
#Output the compliment and reverse of the sequence above

EcoRI_start = dna.find('GAATTC') + 1
EcoRI_end = dna.find('GAATTC') + 1 + 5
#Searching EcoRI site, start and end

front_dna = dna[:396]
back_dna = dna[396:]
front_length = (len(front_dna))
back_length = (len(back_dna))
front_position = '1-397'
back_position = '398-842'
print ('{0}\t{1}\t{2}'.format(front_dna, front_length, front_position))
print ('{0}\t{1}\t{2}'.format(back_dna, back_length, back_position))
#Defining the resulting fragments from EcoRI digest; output is separated by tabs

output = [front_dna, back_dna]
print (sorted(output, key=lambda x: len(x)))
#Sorting sequences in list by length - short to long
