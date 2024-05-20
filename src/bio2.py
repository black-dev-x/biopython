from Bio.Seq import Seq

sequence = Seq("AGTACACTGGTA")

rna_sequence = sequence.transcribe()
dna_sequence = rna_sequence.back_transcribe()

protein_sequence = rna_sequence.translate()
protein_sequence2 = dna_sequence.translate()
protein_sequence3 = sequence.translate()

# three different paths to get the same protein sequence
print(protein_sequence)
print(protein_sequence2)
print(protein_sequence3)
