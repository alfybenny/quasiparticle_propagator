import numpy as np

def scan(index, centroid_list, Rng):
    
    near_ind = [] # centroids near to the given index:
        
    for i in range(0, len(centroid_list)):
        
        R = abs(np.linalg.norm(centroid_list[index]) - np.linalg.norm(centroid_list[i]))

        
        if R < Rng and index != i:
            
            near_ind.append(i)
        
    return near_ind
            
    

