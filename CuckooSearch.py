import random

weights = [10, 20, 30, 40, 50]
values = [60, 100, 120, 240, 300]
capacity = 100

N = 30
GENS = 20
Pa = 0.25

def fitness(solution):
    total_weight = sum(w for w, s in zip(weights, solution) if s > 0.5)
    total_value = sum(v for v, s in zip(values, solution) if s > 0.5)
    return total_value if total_weight <= capacity else 0

def random_solution():
    return [random.random() for _ in range(len(weights))]

def levy_flight(Lambda):
    u = random.gauss(0, 1)
    v = random.gauss(0, 1)
    step = u / abs(v) ** (1 / Lambda)
    return step

def get_cuckoo(sol, best):
    step_size = levy_flight(1.5)
    new_sol = [max(0, min(1, s + step_size * (s - b))) for s, b in zip(sol, best)]
    return new_sol

def abandon_nests(pop, Pa):
    n = len(pop)
    for i in range(n):
        if random.random() < Pa:
            pop[i] = random_solution()

nests = [random_solution() for _ in range(N)]
best = max(nests, key=fitness)

for _ in range(GENS):
    for i in range(N):
        new_sol = get_cuckoo(nests[i], best)
        if fitness(new_sol) > fitness(nests[i]):
            nests[i] = new_sol
    abandon_nests(nests, Pa)
    new_best = max(nests, key=fitness)
    if fitness(new_best) > fitness(best):
        best = new_best
    print(f"Best value = {fitness(best)}")

binary_best = [1 if x > 0.5 else 0 for x in best]
print("\nBest solution:", binary_best)
print("Total value:", fitness(binary_best))
print("Total weight:", sum(w for w, x in zip(weights, binary_best) if x))
