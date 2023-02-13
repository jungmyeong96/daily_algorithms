import sys

N = int(sys.stdin.readline())

subsequence = list(map(int, sys.stdin.readline().split()))

dp = [0] * 1001

count = 0

for i in range(N):
    for j in range(i):
        if subsequence[i] > subsequence[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))