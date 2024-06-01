from Bio.PDB import *

# SMCRA: Structure, Model, Chain, Residue, Atom

parser = PDBParser()
structure = parser.get_structure("1BGA", "./1bga.pdb")

length = len(structure)
print(length)

first_model = structure[0]

a_chain = first_model['A']
residue_100 = a_chain[100]

carbon_atom_100 = residue_100['CA']

carbon_atom_101 = structure[0]['A'][101]['CA']

distance = carbon_atom_100 - carbon_atom_101

print(distance)
