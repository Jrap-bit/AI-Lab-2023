import random
import matplotlib.pyplot as plt

# Define the set to partition
numbers = [10, 20, 15, 5, 25]

# Define the genetic algorithm parameters
POPULATION_SIZE = 10
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
GENERATIONS = 100

# Define the fitness function
def fitness(solution):
    sum1 = sum([numbers[i] for i in range(len(numbers)) if solution[i]])
    sum2 = sum([numbers[i] for i in range(len(numbers)) if not solution[i]])
    diff = abs(sum1 - sum2)
    return 1 / (diff + 1)

# Roulette Wheel Selection Function
def roulette_wheel_selection(fitness_values, population):
    selected = []
    total_fitness = sum(fitness_values)
    for _ in range(len(population)):
        threshold = random.uniform(0, total_fitness)
        fitness_sum = 0
        for i in range(len(population)):
            fitness_sum += fitness_values[i]
            if fitness_sum > threshold:
                selected.append(population[i])
                break
    return selected

# Elitist Selection Function
def elitist_selection(fitness_values, population):
    selected = []
    best_solutions = [population[i] for i in sorted(range(len(fitness_values)), key=lambda k: fitness_values[k])[:2]]
    selected.extend(best_solutions)
    return selected

# Genetic Algorithm using Roulette Wheel Selection
def genetic_algorithm_roulette():
    # Create the initial population
    population = [[random.randint(0, 1) for _ in range(len(numbers))] for _ in range(POPULATION_SIZE)]

    # Main loop of the genetic algorithm
    min_fitness_values = []
    avg_fitness_values = []
    for generation in range(GENERATIONS):
        # Evaluate the fitness of each solution
        fitness_values = [fitness(solution) for solution in population]
        min_fitness = min(fitness_values)
        min_fitness_values.append(min_fitness)
        avg_fitness = sum(fitness_values) / len(fitness_values)
        avg_fitness_values.append(avg_fitness)

        # Select parents for the next generation using roulette wheel selection
        parents = roulette_wheel_selection(fitness_values, population)

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
        population = offspring

    # Find the best solution
        fitness_values = [fitness(solution) for solution in population]
        best_solution = population[fitness_values.index(max(fitness_values))]
        subset1 = [numbers[i] for i in range(len(numbers)) if best_solution[i]]
        subset2 = [numbers[i] for i in range(len(numbers)) if not best_solution[i]]
        print("Best solution found: ", subset1, "and", subset2)

        # Plot the fitness values
        min_fitness = min(fitness_values)
        avg_fitness = sum(fitness_values) / len(fitness_values)
        min_fitness_values.append(min_fitness)
        avg_fitness_values.append(avg_fitness)

        # Perform elitist selection
        elites = []
        elites_fitness = []
        for i in range(ELITISM_SIZE):
            elite_index = fitness_values.index(max(fitness_values))
            elites.append(population[elite_index])
            elites_fitness.append(fitness_values[elite_index])
            population.pop(elite_index)
            fitness_values.pop(elite_index)

        # Perform roulette wheel selection
        selected = []
        for i in range(POPULATION_SIZE - ELITISM_SIZE):
            parents = roulette_wheel_selection(population, fitness_values, 2)
            selected.append(parents[0])
            selected.append(parents[1])

        # Combine the elites and the selected solutions
        population = elites + selected

        # Perform crossover and mutation
        for i in range(0, POPULATION_SIZE - ELITISM_SIZE, 2):
            parent1 = population[i]
            parent2 = population[i + 1]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutation(child1)
            child2 = mutation(child2)
            population[i] = child1
            population[i + 1] = child2

    # Find the best solution after all generations
    fitness_values = [fitness(solution) for solution in population]
    best_solution = population[fitness_values.index(max(fitness_values))]
    subset1 = [numbers[i] for i in range(len(numbers)) if best_solution[i]]
    subset2 = [numbers[i] for i in range(len(numbers)) if not best_solution[i]]
    print("Best solution found: ", subset1, "and", subset2)

    # Plot the fitness values
    plt.plot(min_fitness_values, label='Min Fitness')
    plt.plot(avg_fitness_values, label='Avg Fitness')
    plt.legend()
    plt.show()

