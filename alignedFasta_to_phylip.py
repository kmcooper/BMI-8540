from Bio import AlignIO
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file) as handle:
    records = AlignIO.parse(handle, "fasta")
    with open(output_file, "w") as output_handle:
        AlignIO.write(records, output_handle, "phylip")
