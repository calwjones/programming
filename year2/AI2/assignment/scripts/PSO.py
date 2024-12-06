import pyswarms as ps
import numpy as np

# Define bounds for Function 1
bounds_1 = (np.array([-10] * 20), np.array([10] * 20))

# PSO Options for Function 1
options_1 = {'c1': 0.5, 'c2': 0.5, 'w': 0.7}

# Instantiate optimizer for Function 1
optimizer_1 = ps.single.GlobalBestPSO(n_particles=50, dimensions=20, options=options_1, bounds=bounds_1)

# Define your fitness function (example for Function 1)
def function_1(x):
    fitness_values = []
    d = 20
    for particle in x:
        utility = (particle[0] - 1) ** 2
        for i in range(1, d):
            utility += i * ((2 * (particle[i] ** 2) - particle[i - 1]) ** 2)
        fitness_values.append(utility)
    return np.array(fitness_values)

# Perform optimization for Function 1
best_cost_1, best_pos_1 = optimizer_1.optimize(function_1, iters=200)
print(f"Best fitness for Function 1: {best_cost_1}")

# Define bounds for Function 2
bounds_2 = (np.array([-500] * 20), np.array([500] * 20))

# PSO Options for Function 2
options_2 = {'c1': 0.5, 'c2': 0.5, 'w': 0.9}

# Instantiate optimizer for Function 2
optimizer_2 = ps.single.GlobalBestPSO(n_particles=50, dimensions=20, options=options_2, bounds=bounds_2)

# Define your fitness function (example for Function 2)
def function_2(x):
    fitness_values = []
    d = 20
    for particle in x:
        utility = 418.9829 * d
        for value in particle:
            utility -= value * np.sin(np.sqrt(abs(value)))
        utility += 31
        fitness_values.append(utility)
    return np.array(fitness_values)

# Perform optimization for Function 2
best_cost_2, best_pos_2 = optimizer_2.optimize(function_2, iters=250)
print(f"Best fitness for Function 2: {best_cost_2}")