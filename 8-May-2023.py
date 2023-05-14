"""
    8-May-2023.py
    Made by: Parjanya Pandey
    BT20HCS216
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def fitness(individual, A):
    f = sum(a * (2 * p - 1) for a, p in zip(A, individual))
    return 1 / (abs(f) + 1)


def roulette(population, fitness_vals):
    total_fitness = sum(fitness_vals)
    sel_prob = [f / total_fitness for f in fitness_vals]
    return population[np.random.choice(len(population), 2, p=sel_prob)]


def crossover_selection(parents, crossover_rate=0.8):
    if random.random() < crossover_rate:
        cross_pt = random.randint(1, len(parents[0]) - 1)
        return np.vstack(([np.hstack((parents[0][:cross_pt], parents[1][cross_pt:])),
                           np.hstack((parents[1][:cross_pt], parents[0][cross_pt:]))]))
    else:
        return parents


def mutation_function(new_offsprings, mutation_rate=0.1):
    for child in new_offsprings:
        for i in range(len(child)):
            if random.random() < mutation_rate:
                child[i] = 1 - child[i]
    return new_offsprings


def find_best_individuals(population, fitness_vals, num_best):
    best_indices = np.argpartition(fitness_vals, -num_best)[-num_best:]
    return population[best_indices]


def genetic_algorithm(size_of_nums, num_arr, method_name):
    population_size = 10
    generations = 100
    elitist_size = 2
    population = np.random.randint(2, size=(population_size, size_of_nums))
    min_fitness = []
    avg_fitness_vals = []

    for generation in range(generations):
        fitness_vals = [fitness(individual, num_arr) for individual in population]
        min_fitness.append(1 / max(fitness_vals))
        avg_fitness_vals.append(1 / np.mean(fitness_vals))

        new_population = []

        if method_name == "mixed":
            new_population = find_best_individuals(population, fitness_vals, elitist_size).tolist()

        for _ in range((population_size - (elitist_size if method_name == "mixed" else 0)) // 2):
            parents = roulette(population, fitness_vals)
            new_offsprings = crossover_selection(parents)
            new_offsprings = mutation_function(new_offsprings)
            new_population.extend(new_offsprings)

        population = np.array(new_population)

    return min_fitness, avg_fitness_vals


N = 11
A = [10, 20, 15, 5, 25, 30, 40, 35, 45, 55, 50]

selection_method = "roulette"
min_fitness_values, avg_fitness = genetic_algorithm(N, A, selection_method)

plt.plot(min_fitness_values, label="Minimum f")
plt.plot(avg_fitness, label="Average f")
plt.xlabel("Generation")
plt.ylabel("Value of F")
plt.legend()
plt.show()

selection_method = "mixed"
min_fitness_values, avg_fitness = genetic_algorithm(N, A, selection_method)

plt.plot(min_fitness_values, label="Minimum f")
plt.plot(avg_fitness, label="Average f")
plt.xlabel("Generation")
plt.ylabel("Value of F")
plt.legend()
plt.show()
