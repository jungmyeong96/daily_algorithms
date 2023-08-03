import sys
import time

# start = time.time()

k, p, n = map(int, sys.stdin.readline().split())


#k *= p ** n

for i in range(n):
    k = k * p % 1000000007
print(k)

# end = time.time()

# print("time", end - start)
