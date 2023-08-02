import sys
import math

# Diamond-Square-Algorithm
# N번의 횟수 마다 각 변의 중앙과 중심에 점을 추가
# 변에 존재하는 점의 갯수의 제곱이 총 갯수


n = int(sys.stdin.readline())

dp = [0 for _ in range(16)]

dp[0] = 2

size = 3
result = 0
for i in range(1, n + 1):
    dp[i] += dp[i - 1] + (2**(i-1))
print(dp[n] ** 2)
