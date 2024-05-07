def show_file(filename: str):
  file = open(filename)
  lines = file.readlines()
  print("".join(lines))
  
if __name__ == "__main__":
  show_file("second.fasta")
