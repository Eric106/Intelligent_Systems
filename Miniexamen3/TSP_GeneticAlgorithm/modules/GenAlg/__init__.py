from . import population as pop
import numpy as np
import pandas as pd


# define custom fitness function:
def get_tot_dist(order_of_cities_visited):
    tot_dist = 0
    for i in range(0, len(order_of_cities_visited)-1) :
        city1 = order_of_cities_visited[i]
        city2 = order_of_cities_visited[i+1]
        tot_dist += distances_df.iloc[(city1,city2)]
    arbitrary_big_negative = -10000
    return arbitrary_big_negative + tot_dist

def solve_TSP(distanceMatrix):
    global distances_df
    # distances_df = pd.read_csv(fileNameCSV, index_col=0)
    distances_df = distanceMatrix
    print(distances_df)
    pop_number = 20
    size_of_genotype = len(distances_df.columns)
    p = pop.Population(pop_number, size_of_genotype, get_tot_dist) 
    

    max_gen = 3200 
    i=0
    while i < max_gen:
        if i % 50 == 0 :
            print('.')
        if(i % 300 == 0) : 
            print('temporary best fitness: ', p.evaluate()[0].fitness, 
                ' distance: ', p.evaluate()[0].fitness+ 10000)
        p.next_gen(3)
        i+=1
        
    print('final best fitness : ', p.evaluate()[0].fitness, ' distance: ', 
                p.evaluate()[0].fitness+10000)
    print('final best genotype : ', p.evaluate()[-1].genotype)