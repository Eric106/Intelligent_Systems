import numpy as np
import random
import numbers
import copy as cop

class Agent :

    genotype = []
    length = 0
    fitness = 0
 
    
    def __init__(self, length_or_genotype, fitness_func) :
        
        if isinstance(length_or_genotype, numbers.Number) :
            self.length = length_or_genotype
            self.genotype = np.random.permutation(length_or_genotype)
        else:
            self.genotype = length_or_genotype
            self.length = len(length_or_genotype)
        self.fitness_func = fitness_func 
            
    def copy(self) :
        return cop.copy(self)
        
    def reset_genotype(self):
        self.genotype = np.random.permutation(self.length)
        return self
    
    def set_genotype(self, genotype):
        self.genotype = genotype
        self.length = len(genotype)
        return self.genotype
        
    def evaluate(self):
        self.fitness = self.fitness_func(self.genotype)
        return self
        
    def try_mutate(self, chance_as_n_between_0_and_1=0.1) :
        if random.uniform(0, 1) < chance_as_n_between_0_and_1:
            element1 = 0
            element2 = 0
            while element1 == element2 :
                element1 = random.randrange(self.length)
                element2 = random.randrange(self.length)
            temp = self.genotype[element1]
            self.genotype[element1] = self.genotype[element2]
            self.genotype[element2] = temp
        return self        