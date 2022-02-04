from abc import abstractmethod
import numpy as np

class Couple:
    
    epsilon = 8.854e-12 # Unit Fm-1
    
    def __init__(self, coor_A, coor_B, prop_A, prop_B):
        self.coor_A = coor_A
        self.coor_B = coor_B
        self.prop_A = prop_A
        self.prop_B = prop_B
    
    @abstractmethod
    def J(self):
        pass
    
class dip_dip(Couple):
    
    def J(self):
        
        # Unit vectors of two dipoles (Belongs to molecule A and B)
        unit_A = self.prop_A/np.linalg.norm(self.prop_A)
        unit_B = self.prop_B/np.linalg.norm(self.prop_B)
        
        # Distance vector between two centroids 
        R = self.coor_B - self.coor_A
        
        unit_R = R/np.linalg.norm(R)
        
        # k is the orientation factor
        k = np.dot(unit_A, unit_B) - 3*np.dot(unit_A, unit_R)*np.dot(unit_B, unit_R)
        
        # Converting the value to Debyee
        mag_u1 = np.linalg.norm(self.prop_A)*3.3356e-30
        mag_u2 = np.linalg.norm(self.prop_B)*3.3356e-30
        mag_R = np.linalg.norm(R)*1e-10 # Converting angstrom to meters
        
        # Calculation of dipole dipole coupling
        hab = (1/(4*np.pi*self.epsilon))*k*(mag_u1*mag_u2)/(mag_R)**3
        return hab
        
class trans_charge(Couple):
    pass

class trans_dens(Couple):
    pass

class mol_orb(Couple):
    pass
        