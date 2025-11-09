import random
import math

# Distance matrix for TSP (example with 5 cities)
dist = [
    [0, 2, 9, 10, 7],
    [1, 0, 6, 4, 3],
    [15, 7, 0, 8, 3],
    [6, 3, 12, 0, 11],
    [9, 7, 5, 6, 0]
]

NUM_CITIES = len(dist)
NUM_ANTS = 20
GENS = 20
ALPHA = 1.0
BETA = 5.0
RHO = 0.5
Q = 100

pheromone = [[1 for _ in range(NUM_CITIES)] for _ in range(NUM_CITIES)]

def distance(path):
    return sum(dist[path[i]][path[(i + 1) % NUM_CITIES]] for i in range(NUM_CITIES))

def probability(i, j, visited):
    tau = pheromone[i][j] ** ALPHA
    eta = (1 / dist[i][j]) ** BETA if dist[i][j] != 0 else 0
    return 0 if j in visited else tau * eta

best_path = None
best_length = float("inf")

for _ in range(GENS):
    all_paths = []
    for ant in range(NUM_ANTS):
        path = [random.randint(0, NUM_CITIES - 1)]
        while len(path) < NUM_CITIES:
            i = path[-1]
            probs = [probability(i, j, path) for j in range(NUM_CITIES)]
            total = sum(probs)
            if total == 0:
                next_city = random.choice([j for j in range(NUM_CITIES) if j not in path])
            else:
                r = random.random() * total
                s = 0
                for j, p in enumerate(probs):
                    s += p
                    if s >= r:
                        next_city = j
                        break
            path.append(next_city)
        all_paths.append(path)

    for i in range(NUM_CITIES):
        for j in range(NUM_CITIES):
            pheromone[i][j] *= (1 - RHO)

    for path in all_paths:
        L = distance(path)
        for i in range(NUM_CITIES):
            a, b = path[i], path[(i + 1) % NUM_CITIES]
            pheromone[a][b] += Q / L

    best_local = min(all_paths, key=distance)
    best_local_len = distance(best_local)
    if best_local_len < best_length:
        best_path = best_local[:]
        best_length = best_local_len

    print(f"Best length = {best_length}")

print("\nBest path:", best_path)
print("Total distance:", best_length)
