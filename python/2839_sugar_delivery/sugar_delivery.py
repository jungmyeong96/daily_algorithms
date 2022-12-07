target = int(input())

dp = [0] * 5001

dp[3] = dp[5] = 1

for idx in range(1, target + 1):
    if dp[idx - 3]:
        dp[idx] = dp[idx - 3] + 1
    if dp[idx - 5]:
        dp[idx] = min(dp[idx], dp[idx - 5] + 1) if dp[idx] else dp[idx - 5] + 1

print(dp[target] if dp[target] else -1)
