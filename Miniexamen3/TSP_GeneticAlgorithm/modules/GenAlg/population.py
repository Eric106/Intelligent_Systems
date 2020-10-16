from . import agent as ag
import numpy as np
import random
import copy as cp
from . import sort

class Population :


    length = 0
    members = []
    


    def __init__(self, pop_len, ag_len, fitness_func) :
        self.length = pop_len
        self.members = np.empty(pop_len, dtype=object)
        for i in range(0, self.length) :
            self.members[i] = ag.Agent(ag_len, fitness_func)
            
    def crossover(self, agentX, agentY) :
        child1_gen = np.empty(agentX.length)
        child1_gen.fill(np.NaN)
        child2_gen = np.empty(agentY.length)
        child2_gen.fill(np.NaN)
    
        piece_len = np.floor(agentX.length/3.0 + 0.5)
        starting_el = int(random.randrange(agentX.length - piece_len))
        end_el = int(starting_el+piece_len)
        
        def trans_rest(agent1, agent2, child_gen):
            
            child_gen[starting_el:end_el] = agent2.genotype[starting_el:end_el]
            
            
            i=end_el-1
            j=end_el-1
            
            while True:
                i+=1
                if i > agent1.length - 1 :
                    i -= agent1.length
                if i == starting_el:
                    break
                while agent1.genotype[j] in child_gen :
                    j+=1
                    if j > agent1.length - 1 :
                        j -= agent1.length
                    if j == end_el-1 :
                        break
                child_gen[i] = agent1.genotype[j]
                    
            return child_gen.astype(int)
      
        child1_gen = trans_rest(agentX, agentY, child1_gen)
        child2_gen = trans_rest(agentY, agentX, child2_gen)
                      
        childX = ag.Agent(child1_gen, agentX.fitness_func)
        childY = ag.Agent(child2_gen, agentX.fitness_func)
        
        return(childX, childY)

    def roulette_wheel(self, times = 1):
        prob = np.empty(self.length)
        parents_i = np.empty(times*2)        
        for i in range (0, times*2, 2): 
            
            def choose_parent():
                tot_fitness = 0
                for ind in self.members:
                    tot_fitness += ind.fitness
                prob[0] = self.members[0].fitness / tot_fitness
                for j in range (1, self.length):
                    prob[j] = self.members[j].fitness / tot_fitness + prob[j-1]
                fate = np.random.rand(1)
                p=0
                while fate > prob[p]:
                    p+=1
                return p

            parent_ind1 = choose_parent()
            parent_ind2 = choose_parent()
        
            
            while (parent_ind1 == parent_ind2) :
                parent_ind2 = choose_parent()
            
            parents_i[i] = parent_ind1
            parents_i[i+1] = parent_ind2
            
        return parents_i
    
    def evaluate(self):
        for ind in self.members:
            ind.evaluate()
        sort.mergeSort(self.members)
        return self.members
    
    def next_gen(self, couples = 1):
        self.evaluate()
            
        parent_indeces = self.roulette_wheel(couples).astype(int)
        
        for i in range (0, len(parent_indeces), 2):
            p1 = self.members[parent_indeces[i]]
            p2 = self.members[parent_indeces[i+1]]
            c1, c2 = self.crossover(p1, p2)
            self.members[-(i+1)] = c1.try_mutate()
            self.members[-(i+2)] = c2.try_mutate()
            
        return self.members
             