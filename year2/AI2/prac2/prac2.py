import random 
import copy
import matplotlib.pyplot as plt
P = 50
N = 50
MUTRATE = 1/N
GENERATIONS = 50

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

avg_fit_off_list = []
best_fit_off_list = []

for generation in range(GENERATIONS):
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

    toff1 = Individual()
    toff2 = Individual()
    temp = Individual()
    for i in range( 0, P, 2 ):
        toff1 = copy.deepcopy(offspring[i])
        toff2 = copy.deepcopy(offspring[i+1])
        temp = copy.deepcopy(offspring[i])
        crosspoint = random.randint(1,N)
        for j in range (crosspoint, N):
            toff1.gene[j] = toff2.gene[j]
            toff2.gene[j] = temp.gene[j]
        offspring[i] = copy.deepcopy(toff1)
        offspring[i+1] = copy.deepcopy(toff2)

    for i in range( 0, P ):
        newind = Individual()
        newind.gene = []
        for j in range( 0, N ):
            gene = offspring[i].gene[j]
            mutprob = random.random()
            if mutprob < MUTRATE:
                if( gene == 1):
                    gene = 0
                else:
                    gene = 1
            newind.gene.append(gene)

        offspring[i] = newind

    for ind in offspring:
        ind.fitness = test_function(ind)

    total_fit_pop = sum(ind.fitness for ind in population)
    total_fit_off = sum(ind.fitness for ind in offspring)

    avg_fit_pop = total_fit_pop / P
    avg_fit_off = total_fit_off / P

    best_fit_pop = max(population, key=lambda ind: ind.fitness)
    best_fit_off = max(offspring, key=lambda ind: ind.fitness)
    best_fit_pop_num = max(ind.fitness for ind in population)
    best_fit_off_num = max(ind.fitness for ind in offspring)

    print(f"Generation {generation + 1}:")
    print(f"total population fitness: {total_fit_pop}, total offspring fitness: {total_fit_off}")
    print(f"avg population fitness: {avg_fit_pop}, avg offspring fitness: {avg_fit_off}")
    print(f"best population fitness: {best_fit_pop_num}, best offspring fitness: {best_fit_off_num}\n")

#    if best_fit_pop>best_fit_off:
#        print()
#    elif avg_fit_pop>avg_fit_off:
#        print()
#    elif total_fit_pop>total_fit_off:
#        print()
#    else:    

    best_index_off = offspring.index(best_fit_off)
    if best_fit_pop.fitness>best_fit_off.fitness:
        offspring[best_index_off] = copy.deepcopy(best_fit_pop)
    population = copy.deepcopy(offspring)

    avg_fit_off_list.append(avg_fit_off)
    best_fit_off_list.append(max(ind.fitness for ind in offspring))


print(f"Avg fitness list length: {len(avg_fit_off_list)}")
print(f"Best fitness list length: {len(best_fit_off_list)}")
plt.plot(range(1, GENERATIONS + 1), avg_fit_off_list, label='Average Offspring Fitness')
plt.plot(range(1, GENERATIONS + 1), best_fit_off_list, label='Best Offspring Fitness')
plt.title('Offspring Fitness over Generations')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.legend()
plt.grid()
plt.show()

