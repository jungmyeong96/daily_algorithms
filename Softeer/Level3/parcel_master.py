import sys
from itertools import permutations

n, m, k = map(int, sys.stdin.readline().split())

rails = list(map(int, sys.stdin.readline().split()))

all_case = permutations(rails)
weights = []

for case in all_case:
    total = 0
    idx = 0
    for i in range(k):
        basket = 0
        while True:
            basket += case[idx]
            idx += 1
            idx %= n
            if basket + case[idx] > m:
                break
        total += basket
    weights.append(total)

print(min(weights))


