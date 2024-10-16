import random 
import copy
P = 50
N = 10

class Individual:
    def __init__(self):
        self.gene = [0]*N
        self.fitness = 0

population = []
for x in range (0, P):
    tempgene=[]
    for y in range (0, N):
        tempgene.append( random.randint(0,1))
    newind = Individual()
    newind.gene = tempgene.copy()
    population.append(newind) 

def test_function( ind ):
    utility=0
    for i in range(N):
        utility = utility + ind.gene[i]
    return utility 

for ind in population:
    ind.fitness = test_function(ind)

offspring = []

for i in range (0, P):
    parent1 = random.randint( 0, P-1 )
    off1 = copy.deepcopy(population[parent1])
    parent2 = random.randint( 0, P-1 )
    off2 = copy.deepcopy(population[parent2])
    if off1.fitness > off2.fitness:
        offspring.append( off1 )
    else:
        offspring.append( off2 )

for ind in offspring:
    ind.fitness = test_function(ind)

total_fit_pop = sum(ind.fitness for ind in population)
total_fit_off = sum(ind.fitness for ind in offspring)

print(f"total population: {total_fit_pop}, total offspring: {total_fit_off}")

avg_fit_pop = total_fit_pop/P
avg_fit_off = total_fit_off/P

print(f"avg population: {avg_fit_pop}, avg offspring: {avg_fit_off}")

best_fit_pop = max(ind.fitness for ind in population)
best_fit_off = max(ind.fitness for ind in offspring)

print(f"best population fitness: {best_fit_pop}, best offspring fitness: {best_fit_off}")
