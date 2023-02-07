import sys

n = int(sys.stdin.readline())

dp = [0] * 101

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2


for _ in range(n):
    num = int(sys.stdin.readline().strip())
    for idx in range(5, num + 1):
        dp[idx] = dp[idx - 2] + dp[idx - 3]
    print(dp[num])

