import random
import math

POP_SIZE = 100
GENS = 20
MUT_RATE = 0.2
FUNC = lambda x: x**4 + 3*x**3 - 2*x**2 - 5*x + 10  # function to minimize
RANGE = (-10, 10)

def random_gene():
    return random.uniform(*RANGE)

def fitness(x):
    return 1 / (1 + FUNC(x)**2)

def selection(pop):
    a, b = random.choice(pop), random.choice(pop)
    return a if fitness(a) > fitness(b) else b

def crossover(p1, p2):
    return (p1 + p2) / 2

def mutate(gene):
    if random.random() < MUT_RATE:
        gene += random.uniform(-1, 1)
        gene = max(min(gene, RANGE[1]), RANGE[0])
    return gene

population = [random_gene() for _ in range(POP_SIZE)]

for _ in range(GENS):
    new_pop = []
    for _ in range(POP_SIZE):
        p1, p2 = selection(population), selection(population)
        child = crossover(p1, p2)
        child = mutate(child)
        new_pop.append(child)
    population = new_pop
    best = min(population, key=FUNC)
    print(f"Best value = {FUNC(best):.6f} at x = {best:.4f}")

best = min(population, key=FUNC)
print("\nMinimized value:", FUNC(best))
print("At x =", best)
print("Function:", FUNC)

