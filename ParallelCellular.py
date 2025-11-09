import random
import time

# Parameters
ROAD_LENGTH = 50
NUM_CARS = 15
V_MAX = 5
P_SLOW = 0.3
STEPS = 20

# Initialize road: -1 means empty cell
road = [-1] * ROAD_LENGTH
positions = random.sample(range(ROAD_LENGTH), NUM_CARS)
for i, pos in enumerate(positions):
    road[pos] = random.randint(0, V_MAX)

def display(road):
    s = ''.join('C' if x != -1 else '.' for x in road)#C stands for car
    print(s)

for step in range(STEPS):
    new_road = [-1] * ROAD_LENGTH
    # Step 1: Acceleration
    for i in range(ROAD_LENGTH):
        if road[i] != -1:
            v = min(road[i] + 1, V_MAX)
            road[i] = v

    # Step 2: Slowing down due to other cars
    for i in range(ROAD_LENGTH):
        if road[i] != -1:
            d = 1
            while d <= road[i] and road[(i + d) % ROAD_LENGTH] == -1:
                d += 1
            road[i] = min(road[i], d - 1)

    # Step 3: Random slowdown
    for i in range(ROAD_LENGTH):
        if road[i] > 0 and random.random() < P_SLOW:
            road[i] -= 1

    # Step 4: Move cars (parallel update)
    for i in range(ROAD_LENGTH):
        if road[i] != -1:
            new_pos = (i + road[i]) % ROAD_LENGTH
            new_road[new_pos] = road[i]

    road = new_road
    print(f"Step {step+1:02d}:", end=' ')
    display(road)
    time.sleep(0.05)
