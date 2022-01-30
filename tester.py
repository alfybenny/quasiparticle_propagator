import input_interpreter as inp

filename = 'combined.xyz'

system = inp.xyz(42, filename)
system.readfile()

M = system.indexify()
L = system.mol_coor(1)


# k = system.molecule(i)
# k.cent()
# k.quasi_type()
# k.quasi_state()


print(len(M[1]))
print(L)