#/usr/bin/python3

import sys
file = sys.argv[1]
fileContents = open(file,"r")

currLine = fileContents.readline()
sequence = ''
while(currLine):
  currLine = currLine.rstrip()
  if(currLine.startswith('>')):
    if(sequence):
      for nucPosition in range(0,len(sequence),3):
        print(sequence[nucPosition:nucPosition+3],end="\t")
      sequence = ''
      print("\n")
    print("Codons for " + currLine)
  elif(currLine):
    sequence = sequence + currLine
  currLine = fileContents.readline()
  if not currLine:
    if(sequence):
      for nucPosition in range(0,len(sequence),3):
        print(sequence[nucPosition:nucPosition+3],end="\t")
      sequence = ''
      print()
