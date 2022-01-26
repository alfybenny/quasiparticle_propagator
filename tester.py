import input_interpreter as inp

filename = 'combined.xyz'

system = inp.xyz(42, filename)
system.readfile()
M = system.extract_coordinate()


k = system.molecule(i)
k.cent()
k.quasi_type()
k.quasi_state()


print(M)