# KMC

import random
import numpy as np

def site_selector(array, mol_index):
    
    rate_sum = 0;
    for i in array:
        
        rate_sum += i
        
    total_sum = rate_sum
    
    prob = random.uniform(0, 1)
    p1 = total_sum*prob
    
    print(prob)
    print(p1)
    print(total_sum)
    rate_sum = 0.0;
    for i in range(0, len(array)):
        
        rate_sum += array[i]
        
        if p1 < rate_sum:
            next_site = mol_index[i]
            array_index = i
            break
        else:
            pass
        
    
    
    p2 = random.uniform(0, 1)
    
    dt = (1/total_sum)*np.log(1/p2)
    
    ret = [0]*2
    
    ret[0] = next_site
    ret[1] = dt
    

    return ret
    