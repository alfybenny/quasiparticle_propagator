
from abc import abstractmethod

class Property:
    
    # Atributes
    
    centroid_list = []
    
    @abstractmethod
    def mon_data():
        pass
    
    def coor_to_cent(self, array, no_of_atoms):
        
        self.centroid_list = [] # Empty list containing centroids
        for i in array:
            
            k = 0
            
            for j in i:
                
                k += j
            self.centroid_list.append(k/no_of_atoms)
            
        return self.centroid_list
               


class trans_dip(Property):
    
    
    # Data associated with a monomer
    def mon_data(): 
        return [1, 1, 1]


class trans_charge(Property):
    pass

class trans_dens(Property):
    pass

class mol_orb(Property):
    pass

