from abc import abstractmethod
import numpy as np
from scipy import constants

class Rate:
    
    def __init__(self, J, l, T):
        self.J = J # Coupling
        self.l = l # Reorganization
        self.T = T # Temperature
                
    @abstractmethod    
    def k_ab():
        pass


class marcus(Rate):
    
    def k_ab(self):
        
        kb = constants.Boltzmann
        hbar = constants.hbar
        
        k_ab = 10**-12 * (2*np.pi/hbar)*(np.sqrt(1/(4*np.pi*kb*self.T*self.l))*(self.J**2)*np.exp(-(self.l/4*kb*self.T)))
        return k_ab
    
    
class FRET(Rate):
    
    def k_ab(self):
        pass
        