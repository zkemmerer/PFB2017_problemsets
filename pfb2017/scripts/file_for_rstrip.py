#!/usr/bin/python3

file_object = open("../files/seq.nt.fa","r")
for line in file_object:
  line = line.rstrip()
  print(line)
