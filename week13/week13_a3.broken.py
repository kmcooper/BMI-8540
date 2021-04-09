from Bio import SeqUtils
from Bio.Seq import Seq
from Bio.SeqUtils import GC

userInput = input("Enter a DNA sequence:\t").strip() .lower(
dnaseq = seq(userInput)

print("Analysis:)
print("DNA Sequence (input):\t"+dnaseq)
print("DNA Sequence Length (nt):\t"+str(length(dnaseq)))
print("GC Content:\t"+ round(GC(dnaseq),2))
print("RNA Sequence:\t"+dna.transcribe())
