import random

DIM = 2
POP_SIZE = 30
GENS = 20
a_max = 2
FUNC = lambda x: sum(xi**2 for xi in x)

def random_pos():
    return [random.uniform(-10, 10) for _ in range(DIM)]

wolves = [random_pos() for _ in range(POP_SIZE)]
alpha, beta, delta = None, None, None

for gen in range(GENS):
    wolves.sort(key=FUNC)
    alpha, beta, delta = wolves[0], wolves[1], wolves[2]
    a = a_max - gen * (a_max / GENS)

    new_wolves = []
    for w in wolves:
        new_pos = []
        for d in range(DIM):
            r1, r2 = random.random(), random.random()
            A1, C1 = 2 * a * r1 - a, 2 * r2
            D_alpha = abs(C1 * alpha[d] - w[d])
            X1 = alpha[d] - A1 * D_alpha

            r1, r2 = random.random(), random.random()
            A2, C2 = 2 * a * r1 - a, 2 * r2
            D_beta = abs(C2 * beta[d] - w[d])
            X2 = beta[d] - A2 * D_beta

            r1, r2 = random.random(), random.random()
            A3, C3 = 2 * a * r1 - a, 2 * r2
            D_delta = abs(C3 * delta[d] - w[d])
            X3 = delta[d] - A3 * D_delta

            new_pos.append((X1 + X2 + X3) / 3)
        new_wolves.append(new_pos)
    wolves = new_wolves

    best_val = FUNC(alpha)
    print(f"Generation {gen+1}: Best = {best_val:.6f} at {alpha}")

print("\nBest solution:", alpha)
print("Minimized value:", FUNC(alpha))
print("Function:", FUNC)
