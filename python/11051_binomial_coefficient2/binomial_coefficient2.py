
dp = [[0] * 1001 for _ in range(1001)]

N, K = map(int, input().split())

# def binomial(N, K):
#     if K == 0 or N == K:
#         return 1
#     if dp[N][K] == 0:
#         dp[N][K] = binomial(N - 1, K - 1) + binomial(N - 1, K)
#     return dp[N][K]
# 런타임에러 재귀가 너무 많이 돌음

def binomial(N, K):
    for i in range(N + 1):
        for j in range(min(i, K) + 1):
            if j == 0 or i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i - 1][j]
    return dp[N][K]


print(binomial(N, K) % 10007)