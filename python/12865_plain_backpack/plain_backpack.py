# import sys

# N, K = map(int,sys.stdin.readline().split())

# dp = [[0] * (K + 1) for i in range(N)]
# maxdp = [0] * N

# for i in range(N):
#     W, V = map(int,sys.stdin.readline().strip().split())
#     for j in range(1, K + 1):
#         if W < K and j == W: 
#             dp[i][j] = V
#         if i != 0 and dp[i - 1][j] != 0:
#             dp[i][j] = dp[i - 1][j]
#         if dp[i][j] != 0 and (j + W <= K):
#             dp[i][j + W] = V + dp[i][j]
#     maxdp[i] = max(dp[i])

# print(max(maxdp))


import sys

N, K = map(int,sys.stdin.readline().split())

dp = [0] * (K + 1)
for i in range(N):
    W, V = map(int,sys.stdin.readline().strip().split())
    if W > K:
        continue
    for j in range(K, 0, -1):
        if dp[j] != 0 and (j + W <= K):
            dp[j + W] = max(dp[j + W], V + dp[j])
    dp[W] = max(dp[W], V)

print(max(dp))



    
