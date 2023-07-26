from typing import List
from typing import Tuple

def fractional_knapsack(cargo: List[Tuple[int, int]], capacity: int):
    total_value = 0
    pack = []
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)

    for p in pack:
        if capacity - p[2] > 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            break
    return total_value



cargo = [(4, 12), (2, 1), (10, 4), (1, 1), (2, 2)]
capacity = 15
print("{:.2f}".format(fractional_knapsack(cargo, capacity)))