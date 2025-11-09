import random

weights = [10, 20, 30, 40, 50]
values = [60, 100, 120, 240, 300]
capacity = 100

POP_SIZE = 50
GENS = 10
MUTATION_RATE = 0.05

def fitness(chromosome):
    total_weight = sum(w for w, g in zip(weights, chromosome) if g)
    total_value = sum(v for v, g in zip(values, chromosome) if g)
    return total_value if total_weight <= capacity else 0

def random_chromosome():
    return [random.randint(0, 1) for _ in range(len(weights))]

def selection(population):
    a, b = random.choice(population), random.choice(population)
    return a if fitness(a) > fitness(b) else b

def crossover(p1, p2):
    point = random.randint(1, len(p1) - 1)
    return p1[:point] + p2[point:]

def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]

population = [random_chromosome() for _ in range(POP_SIZE)]

for _ in range(GENS):
    new_population = []
    for _ in range(POP_SIZE):
        parent1 = selection(population)
        parent2 = selection(population)
        child = crossover(parent1, parent2)
        mutate(child)
        new_population.append(child)
    population = new_population
    best = max(population, key=fitness)
    print(f"Best value = {fitness(best)}")

best_solution = max(population, key=fitness)
print("\nBest solution:", best_solution)
print("Total value:", fitness(best_solution))
print("Total weight:", sum(w for w, g in zip(weights, best_solution) if g))
