
from abc import abstractmethod
import numpy as np

class Property:
    
    # Atributes
    
    centroid_list = []
    prop_list = []
    
    def __init__(self, crystal):
        self.crystal = crystal
    
    @abstractmethod
    def mon_data():
        pass
    
    def coor_to_cent(self, no_of_atoms):
        
        self.centroid_list = [] # Empty list containing centroids
        for i in self.crystal:
            
            k = 0
            
            for j in i:
                
                k += j
            self.centroid_list.append(k/no_of_atoms)
            
        return self.centroid_list
               


class trans_dip(Property):
    
    
    # Data associated with a monomer
    def mon_data(self):
        
        def dipole_orienter(v1, v2): # v1, v2, and D are vectors.
            V = np.cross(v1, v2)
            
            mag = np.linalg.norm(V)
            uni_V = V/mag
            
            return uni_V
            
        # dipole = [1, 0, 0]
        
        temp_list = []
        
        for i in self.crystal:

            v1 = i[1] - i[0] # Define X direction

            v2 = i[3] - i[2] # Define Y direction
            
            D = dipole_orienter(v1, v2)
            
            temp_list.append(D)

            
        self.prop_list = temp_list
                        
        


class trans_charge(Property):
    pass

class trans_dens(Property):
    pass

class mol_orb(Property):
    pass

