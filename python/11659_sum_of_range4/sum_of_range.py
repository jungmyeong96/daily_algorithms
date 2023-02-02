# import sys

# N, M = map(int, sys.stdin.readline().split())

# numbers = list(map(int, sys.stdin.readline().split()))

# for _ in range(M):
#     A, B = map(int, sys.stdin.readline().strip().split())
#     sum = 0
#     for idx in range(A - 1, B):
#         sum += numbers[idx]
#     sys.stdout.write("%d\n" % sum)

# 누적합은 dp를 이용하면 빠름

import sys

N, M = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

dp = [0] * (N + 1)

for idx in range(N):
    dp[idx + 1] = dp[idx] + numbers[idx]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().strip().split())
    sum = dp[B] - dp[A - 1]
    sys.stdout.write("%d\n" % sum)