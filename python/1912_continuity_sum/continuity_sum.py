import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

for idx in range(1, n):
    num[idx] = max(num[idx], num[idx - 1] + num[idx]) #합을 저장한 값과 현재 값을 비교해서 구현

print(max(num))