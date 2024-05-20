from Bio.Seq import Seq

my_seq = Seq("AGTACACTGGT")

print(my_seq)

complement = my_seq.complement()
print(complement)

reverse_complement = my_seq.reverse_complement()
print(reverse_complement)

rna_sequence = my_seq.transcribe()

seq_dna = rna_sequence.back_transcribe()
