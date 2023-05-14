import random

# Define the set to partition
numbers = [10, 20, 15, 5, 25]

# Define the genetic algorithm parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
GENERATIONS = 100

# Define the fitness function
def fitness(solution):
    sum1 = sum([numbers[i] for i in range(len(numbers)) if solution[i]])
    sum2 = sum([numbers[i] for i in range(len(numbers)) if not solution[i]])
    return abs(sum1 - sum2)

# Create the initial population
population = [[random.randint(0, 1) for _ in range(len(numbers))] for _ in range(POPULATION_SIZE)]

# Main loop of the genetic algorithm
for generation in range(GENERATIONS):
    # Evaluate the fitness of each solution
    fitness_values = [fitness(solution) for solution in population]

    # Select parents for the next generation
    parents = []
    # Roulette wheel selection
    total_fitness = sum(fitness_values)
    for _ in range(POPULATION_SIZE):
        threshold = random.uniform(0, total_fitness)
        fitness_sum = 0
        for i in range(POPULATION_SIZE):
            fitness_sum += fitness_values[i]
            if fitness_sum > threshold:
                parents.append(population[i])
                break

    # Elitist selection
    best_solution = population[fitness_values.index(min(fitness_values))]
    if best_solution not in parents:
        parents[0] = best_solution

    # Perform crossover
    offspring = []
    for i in range(0, POPULATION_SIZE, 2):
        if random.random() < CROSSOVER_RATE:
            crossover_point = random.randint(1, len(numbers) - 1)
            offspring1 = parents[i][:crossover_point] + parents[i+1][crossover_point:]
            offspring2 = parents[i+1][:crossover_point] + parents[i][crossover_point:]
            offspring.append(offspring1)
            offspring.append(offspring2)
        else:
            offspring.append(parents[i])
            offspring.append(parents[i+1])

    # Perform mutation
    for solution in offspring:
        if random.random() < MUTATION_RATE:
            index = random.randint(0, len(numbers) - 1)
            solution[index] = 1 - solution[index]

    # Create the next generation
    population = parents + offspring

# Find the best solution
fitness_values = [fitness(solution) for solution in population]
best_solution = population[fitness_values.index(min(fitness_values))]
subset1 = [numbers[i] for i in range(len(numbers)) if best_solution[i]]
subset2 = [numbers[i] for i in range(len(numbers)) if not best_solution[i]]

print("Subset 1:", subset1)
print("Subset 2:", subset2)
