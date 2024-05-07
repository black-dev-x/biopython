sequence = input("Type your sequence: ")

file = open("third.fasta","w")
file.write(">seq\n")
file.write(sequence)
file.close()
