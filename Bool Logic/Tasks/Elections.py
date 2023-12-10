import random

def elections_a():
    """Return wins in area_a"""
    area_a = 0
    if random.random() < 0.87:
        area_a = 'A wins'
    else:
        area_a = 'B wins'
    return (area_a)

def elections_b():
    """Return wins in area_b"""
    area_b = 0
    if random.random() < 0.65:
        area_b = 'A wins'
    else:
        area_b = 'B wins'
    return (area_b)

def elections_c():
    """Return wins in area_c"""
    area_c = 0
    if random.random() < 0.17:
        area_c = 'A wins'
    else:
        area_c = 'B wins'
    return (area_c)

candidate_A_wins = 0

for i in range(10_000):
    candidate_A = 0
    candidate_B = 0
    if elections_a() == 'A wins':
        candidate_A = candidate_A + 1
    else:
        candidate_B = candidate_B + 1

    if elections_b() == 'A wins':
        candidate_A = candidate_A + 1
    else:
        candidate_B = candidate_B + 1

    if elections_c() == 'A wins':
        candidate_A = candidate_A + 1
    else:
        candidate_B = candidate_B + 1

    if candidate_A > candidate_B:
        candidate_A_wins = candidate_A_wins + 1
print(f'After holding an election 10,000 times, candidate A will win with probability {candidate_A_wins/10_000:.0%}')
