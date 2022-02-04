import input_interpreter as inp
import mon_prop
import get_nearby
import dim_couple
import dim_rate
import kmc
from matplotlib import pyplot as plt
import numpy as np

filename = 'napth_test.xyz'

system = inp.xyz(18, filename)
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

prop_operator = mon_prop.trans_dip(system.crystal)

prop_operator.coor_to_cent(system.no_of_atoms)


# Testing dipole orienter

# storing dipoles
prop_operator.mon_data()

# print('transition dipoles')
# print(prop_operator.prop_list)

# print('centroids')
print(len(prop_operator.centroid_list))


# Testing kmc

user_index = 10

t = 0.0
T = 1*1e-11

list_t = [int(0)] * len(prop_operator.centroid_list)
list_t[user_index] = int(1)

exciton_list = []
exciton_list.append(list_t)

while t < T:
    
    current_site = list_t.index(1) 
    
    
    
    near_sites = get_nearby.scan(current_site, prop_operator.centroid_list, 3) # 6 ansgtroms as range
    
    # Calculating coupling
    
    print('near sites are ' +str(near_sites))
    
    ##########
    
    j_ab = []
    for i in near_sites: 
        j_calculator = dim_couple.dip_dip(prop_operator.centroid_list[current_site], prop_operator.centroid_list[i], prop_operator.prop_list[current_site], prop_operator.prop_list[i])
        j_ai = j_calculator.J()
        
        j_ab.append(j_ai)
    
    #print('nearby couplings' +str(j_ab))
    # Calculate rate
    
    k_ab = []
    
    for i in j_ab:
        
        l = 4.8e-20
        
        rate_calculator = dim_rate.marcus(i, l, 293)
        
        k_ai = rate_calculator.k_ab()
        
        
        k_ab.append(k_ai)
        
    #print('nearby rates '+str(k_ab))
    # kmc
    
    ret = kmc.site_selector(k_ab, near_sites)
    
    next_index = ret[0]
    ddt = ret[1]
    
    dt = ddt * 1e-12
    
    print('next index is '+ str(next_index))
    print('next time step is '+ str(dt))
    
    list_t = [int(0)] * len(prop_operator.centroid_list)
    list_t[next_index] = int(1)
    
    exciton_list.append(list_t)
    
    
    
    t += dt
    
# plotting

site_list = []
for i in exciton_list:
    site_list.append(i.index(1))

site_list1 = []
for i in exciton_list:
    site_list1.append(prop_operator.centroid_list[i.index(1)])
    
x = []
y = []
z = []

for i in site_list1:
    
    x.append(i[0])
    y.append(i[1])
    z.append(i[2])

ax = plt.axes(projection='3d')
# ax.plot3D(x, y, z, 'gray')
ax.scatter3D(x, y, z, c=z, cmap='Greens');
plt.close()

print(site_list)
site = range(0, len(site_list)) 
plt.plot(site, site_list, 'ro')
plt.show()

    
    
    