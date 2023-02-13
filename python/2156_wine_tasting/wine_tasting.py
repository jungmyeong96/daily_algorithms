import sys

N = int(sys.stdin.readline())

wines = []
dp = []

for i in range(N):
    wines.append(int(sys.stdin.readline().strip()))

dp = [0 for i in range(N)]

#6 10 13 9 8 1
dp[0] = wines[0]
dp[1] = wines[0] + wines[1] 
dp[2] = max(wines[1] + wines[2], wines[0] + wines[2], dp[1]) #현재 위치에서 마시지 않는 경우도 고려

for i in range(3, N):
    dp[i] = max(dp[i - 2] + wines[i], dp[i - 3] + wines[i - 1] + wines[i], dp[i - 1])

print(dp[N - 1])
