import sys

N = int(sys.stdin.readline())

houses = []

for _ in range(N):
    houses.append(list(map(int, sys.stdin.readline().strip().split())))

for idx in range(1, N):
    houses[idx][0] = min(houses[idx - 1][1], houses[idx - 1][2]) + houses[idx][0]
    houses[idx][1] = min(houses[idx - 1][0], houses[idx - 1][2]) + houses[idx][1]
    houses[idx][2] = min(houses[idx - 1][0], houses[idx - 1][1]) + houses[idx][2]

print(min(houses[N - 1][0], houses[N - 1][1], houses[N - 1][2]))