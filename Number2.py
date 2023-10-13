import random

# Define the city map
city_map = {
    'A': {'B': 12, 'C': 10, 'G': 12},
    'B': {'A': 12, 'C': 8, 'D': 12},
    'C': {'A': 10, 'B': 8, 'D': 11, 'E': 3, 'G': 9},
    'D': {'B': 12, 'C': 11, 'E': 11, 'F': 10},
    'E': {'C': 3, 'G': 7, 'F': 6, 'D': 11},
    'F': {'E': 6, 'G': 9, 'D': 10},
    'G': {'A': 12, 'C': 9, 'E': 7, 'F': 9}
}


cities = list(city_map.keys())
start_city = 'A'

# Genetic Algorithm parameters
population_size = 100
num_generations = 1000
mutation_rate = 0.1

def calculate_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += city_map[route[i]][route[i + 1]]
    total_distance += city_map[route[-1]][route[0]]  # Return to start city
    return total_distance

def generate_individual():
    route = cities.copy()
    random.shuffle(route)
    return route

def select_parents(population, fitness_scores):
    # Roulette wheel selection
    total_fitness = sum(fitness_scores)
    probabilities = [fitness / total_fitness for fitness in fitness_scores]
    parent1 = random.choices(population, probabilities)[0]
    parent2 = random.choices(population, probabilities)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    # Order crossover (OX)
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [-1] * len(parent1)
    for i in range(start, end + 1):
        child[i] = parent1[i]
    pointer_p2 = 0
    for i in range(len(parent1)):
        if child[i] == -1:
            while parent2[pointer_p2] in child:
                pointer_p2 += 1
            # Check if the city from parent2 has a direct path with the previous city in the child route
            prev_city = child[i - 1] if i > 0 else child[-1]
            if parent2[pointer_p2] in city_map[prev_city]:
                child[i] = parent2[pointer_p2]
            else:
                # If not, find a city that has a direct path with the previous city
                for city in cities:
                    if city not in child and city in city_map[prev_city]:
                        child[i] = city
                        break
    return child

def mutate(route):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(route)), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]

# Initialize the population
population = [generate_individual() for _ in range(population_size)]

# Main loop
for generation in range(num_generations):
    fitness_scores = [1 / calculate_distance(route) for route in population]
    new_population = []

    # Elitism: Select the best individual from the current population
    best_route = population[fitness_scores.index(max(fitness_scores))]
    new_population.append(best_route)

    while len(new_population) < population_size:
        parent1, parent2 = select_parents(population, fitness_scores)
        child = crossover(parent1, parent2)
        mutate(child)
        new_population.append(child)

    population = new_population

# Find the best route in the final population
best_route = min(population, key=calculate_distance)
best_distance = calculate_distance(best_route)

print(f"Best Route: {best_route}")
print(f"Total Distance: {best_distance}")
