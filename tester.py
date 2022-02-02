import input_interpreter as inp
import mon_prop

filename = 'combined.xyz'

system = inp.xyz(42, filename)
system.readfile()

M = system.indexify()
L = system.mol_coor(1)


# k = system.molecule(i)
# k.cent()
# k.quasi_type()
# k.quasi_state()


# Testing centroid generation

## Testing whether calling crystal will work
# print(system.matrix)

prop_operator = mon_prop.Property()

print(prop_operator.coor_to_cent(system.crystal, system.no_of_atoms))

