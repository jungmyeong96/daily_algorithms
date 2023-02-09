import sys

n = int(sys.stdin.readline())

# stairs = []

# for i in range(n):
#     staires.append(list(int(sys.stdin.readline())))

# k = 1
# for i in range(1, n):
#     for j in range(k):
#         stairs[i].append(stairs[i - 1] + stairs[i])
#         stairs[i].append(stairs[i - 2] + stairs[i])
#     k += 1

stairs = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(n):
    stairs[i] = int(sys.stdin.readline())

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, n):
    dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

print(dp[n - 1])