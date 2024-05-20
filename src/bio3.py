from Bio import SeqIO

def get_sequence_length(filename):
    for record in SeqIO.parse(filename, "fasta"):
        print(record.seq)
      
if __name__ == "__main__":
    print(get_sequence_length("./bio3.fasta"))
