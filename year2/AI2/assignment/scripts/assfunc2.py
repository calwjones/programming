import random 
import copy
import matplotlib.pyplot as plt
import math

P = 50
N = 20
MUTRATE = 0.5
GENERATIONS = 250
MIN = -500
MAX = 500
MUTSTEP = 0.7

class Individual:
    def __init__(self):
        self.gene = [0]*N
        self.fitness = 0

# initialise the population with random individuals
population = []
for x in range (0, P):
    tempgene=[]
    for y in range (0, N):
        tempgene.append(random.uniform(MIN,MAX))
    newind = Individual()
    newind.gene = tempgene.copy()
    population.append(newind) 

def test_function(ind):
    d = 20
    utility=418.9829*d
    for i in range(d):
        utility-=ind.gene[i]*math.sin(math.sqrt(abs(ind.gene[i])))
    utility+=31
    return utility

avg_fit_off_list = []
best_fit_off_list = []

# main evolutionary loop
for generation in range(GENERATIONS):
    for ind in population:
        ind.fitness = test_function(ind)

    offspring = []
    
    # apply mutation to create offspring
    for i in range(0, P):
        newind = Individual()
        newind.gene = []
        for j in range(0, N):
            gene = population[i].gene[j]
            mutprob = random.random()
            if mutprob < MUTRATE:
                alter = random.uniform(-MUTSTEP, MUTSTEP)  # using mutstep and mutrate to mutate 
                gene = gene + alter
                gene = max(MIN, min(MAX, gene))  
            newind.gene.append(gene)
        offspring.append(newind)

        # apply crossover between pairs of offspring
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

    #fitness evaluation
    for ind in offspring:
        ind.fitness = test_function(ind)

    total_fit_pop = sum(ind.fitness for ind in population)
    total_fit_off = sum(ind.fitness for ind in offspring)

    avg_fit_pop = total_fit_pop / P
    avg_fit_off = total_fit_off / P

    best_fit_pop = min(population, key=lambda ind: ind.fitness)
    best_fit_off = min(offspring, key=lambda ind: ind.fitness)
    best_fit_pop_num = min(ind.fitness for ind in population)
    best_fit_off_num = min(ind.fitness for ind in offspring)

     # replace worst offspring with best individual
    worst_fit_off = max(offspring, key=lambda ind: ind.fitness) 
    worst_index_off = offspring.index(worst_fit_off)
    if avg_fit_pop < avg_fit_off:
        offspring[worst_index_off] = copy.deepcopy(best_fit_pop)

        #keep the best solution in the population
    best_index_off = offspring.index(best_fit_off)
    if best_fit_pop.fitness<best_fit_off.fitness:
        offspring[best_index_off] = copy.deepcopy(best_fit_pop)
    population = copy.deepcopy(offspring)

    avg_fit_off_list.append(avg_fit_off)
    best_fit_off_list.append(min(ind.fitness for ind in offspring))


    print(f"Generation {generation + 1}:")
    print(f"total population fitness: {total_fit_pop}, total offspring fitness: {total_fit_off}")
    print(f"avg population fitness: {avg_fit_pop}, avg offspring fitness: {avg_fit_off}")
    print(f"best population fitness: {best_fit_pop_num}, best offspring fitness: {best_fit_off_num}\n")

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

