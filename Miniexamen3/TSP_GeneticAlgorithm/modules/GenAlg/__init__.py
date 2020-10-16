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

def solve_TSP(distanceMatrix,latLongDict):
    global distances_df
    # distances_df = pd.read_csv(fileNameCSV, index_col=0)
    distances_df = distanceMatrix
    print(distances_df)
    pop_number = 80
    size_of_genotype = len(distances_df.columns)
    p = pop.Population(pop_number, size_of_genotype, get_tot_dist) 
    

    max_gen = 3200 
    i=0
    while i < max_gen:
        if i % 50 == 0 :
            print('.')
        if(i % 300 == 0) : 
            newGen = (p.evaluate()[0].fitness,p.evaluate()[0].fitness+ 10000)
            print('Best distance: ', newGen[1])
        p.next_gen(3)
        i+=1
    newGen = (p.evaluate()[0].fitness,p.evaluate()[0].fitness+ 10000)  
    print('Best distance: ', newGen[1])
    best_genoT = p.evaluate()[-1].genotype
    print('final best genotype : ', best_genoT)

    ordered_citites_dict = {}
    listCities = distances_df.columns.tolist()
    idx = 0
    for indexCity in best_genoT:
        idx+=1
        city = listCities[indexCity]
        lat = round(latLongDict["Latitud"][city],6)
        long = round(latLongDict["Longitud"][city],6)
        ordered_citites_dict.update({
            str(idx)+" => "+city:[lat,long]
        })
    print(list(ordered_citites_dict.keys()))
    return ordered_citites_dict