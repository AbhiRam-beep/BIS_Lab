import random

weights = [10, 20, 30, 40, 50]
values = [60, 100, 120, 240, 300]
capacity = 100

POP_SIZE = 50
GENS = 20
W = 0.7
C1 = 1.5
C2 = 1.5

def fitness(position):
    total_weight = sum(w for w, x in zip(weights, position) if x > 0.5)
    total_value = sum(v for v, x in zip(values, position) if x > 0.5)
    return total_value if total_weight <= capacity else 0

particles = [[random.random() for _ in range(len(weights))] for _ in range(POP_SIZE)]
velocities = [[random.uniform(-1, 1) for _ in range(len(weights))] for _ in range(POP_SIZE)]
pbest = [p[:] for p in particles]
pbest_values = [fitness(p) for p in particles]
gbest = max(pbest, key=fitness)

for _ in range(GENS):
    for i in range(POP_SIZE):
        for d in range(len(weights)):
            r1, r2 = random.random(), random.random()
            velocities[i][d] = (W * velocities[i][d] +
                                C1 * r1 * (pbest[i][d] - particles[i][d]) +
                                C2 * r2 * (gbest[d] - particles[i][d]))
            particles[i][d] += velocities[i][d]
            particles[i][d] = max(0, min(1, particles[i][d]))
        fit = fitness(particles[i])
        if fit > pbest_values[i]:
            pbest[i] = particles[i][:]
            pbest_values[i] = fit
    gbest = max(pbest, key=fitness)
    print(f"Best value = {fitness(gbest)}")

binary_solution = [1 if x > 0.5 else 0 for x in gbest]
print("\nBest solution:", binary_solution)
print("Total value:", fitness(binary_solution))
print("Total weight:", sum(w for w, x in zip(weights, binary_solution) if x))
