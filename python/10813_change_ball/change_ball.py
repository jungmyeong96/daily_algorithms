import sys

N, M = map(int,sys.stdin.readline().strip().split())

basket = [i for i in range(N + 1)]

for i in range(M):
    ball1, ball2 = map(int,sys.stdin.readline().strip().split())
    basket[ball1], basket[ball2] = basket[ball2], basket[ball1]

for i in range(1, N + 1):
    sys.stdout.write("%d " %basket[i])