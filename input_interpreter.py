import numpy as np
from abc import abstractmethod
import re



class input_processing:
    
    # Attributes
    # content = content of the file
    # matrix = final matrix with atom type and coordinates
    # crstal = contains the whole system as a system[molecule[coordinates]]
    content = []
    matrix = []
    crystal = []
    
    # filename
    def __init__(self, no_of_atoms, file):
        self.no_of_atoms = no_of_atoms
        self.file = file

    # read the input file------------------------------------------------------
    def readfile(self):
        self.content = open(self.file, 'r')
        return self.content
         
    # Abstract class: Outputs attribute 'matrix'-------------------------------
    @abstractmethod
    def extract_coordinate(self):
        pass
    
    # Give me np.array of xyz coordinates--------------------------------------
    def get_np_array(self):
        
        # Get 'matrix'
        self.matrix = self.extract_coordinate()
        
        # Delete the atom type from 'matrix'
        for i in self.matrix:
            del i[0]
            
        self.matrix = np.array(self.matrix) # Convert 'matrix' to np.array
        self.matrix = self.matrix.astype(np.float) # Convert 'matrix' elements to float
        return np.array(self.matrix)
    
    # Get atom type------------------------------------------------------------
    def get_atom_list(self):
        
        self.matrix = self.extract_coordinate()
        
        return np.array([i[0] for i in self.matrix])
    
    # Define moleules within the total atom xyz file---------------------------
    def indexify(self):
        # M is a matrix containing np.array of xyz coordinate
        # mol_index to store list of coordiates of each molecule
        
        M = self.get_np_array()
        total_atoms = len(M)
        no_of_molecules = total_atoms/self.no_of_atoms
        
        mol_index = []
        count = 0
        for i in range(0, int(no_of_molecules)):
            
            one_molecule = []
            for j in range(0, self.no_of_atoms):
                one_molecule.append(M[j])
            mol_index.append(one_molecule)
            count += self.no_of_atoms
            
        self.crystal = mol_index
        return self.crystal
    
    # Give molecular coordinate------------------------------------------------
    def mol_coor(self, n):
        M = self.crystal
        return M[n]
                
                
        
        

# SUBCLASS-INPUT_PROCESSING====================================================

# 1. Get coordinates from file for .xyz fileformat
# NOTE: class xyz knows what is content
class xyz(input_processing):
    def extract_coordinate(self):
        
        mat = [] # matrix to store coordinate
            
        with self.content as f:
            for line in f:
                line = re.split(' +', line)
                # Remove empty strings from list
                line = list(filter(('').__ne__, line)) 
                # To remove new lines from list
                atom_coor = [] 
                for i in line:
                    i = i.rstrip()
                    atom_coor.append(i)
                mat.append(atom_coor)
                    
            return mat
                   
        self.matrix = mat
        return self.matrix

# 2. Get coordinates from file for .mol2 fileformat
class mol2(input_processing):
    def extract_coordinate(self):
        print("mol2")

# 3. Get coordinates from file for .cif fileformat
class cif(input_processing):
    def extract_coordinate(self):
        print("cif")
        


