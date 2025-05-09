import random

LANE_BITS = 64
TOTAL_LANES = 25
RATE_LANES = 16
CAPACITY_LANES = 9

state = [0] * TOTAL_LANES
nonzero_capacity = 0
rounds = 0

while nonzero_capacity < CAPACITY_LANES:
    rounds += 1
    message_block = [random.getrandbits(LANE_BITS) for _ in range(RATE_LANES)]
    for i in range(RATE_LANES):
        state[i] ^= message_block[i]
    for i in range(RATE_LANES, TOTAL_LANES):
        if state[i] != 0:
            continue
        if random.choice([True, False]):
            state[i] = random.getrandbits(LANE_BITS)
    nonzero_capacity = sum(1 for i in range(RATE_LANES, TOTAL_LANES) if state[i] != 0)

print("Rounds needed to fill all capacity lanes:", rounds)
