import sys

N = int(sys.stdin.readline())


#          각 자리수에서 맨 뒤에 올수 있는 숫자의 개수(0~9)
#          0  1  2  3  4  5  6  7  8  9
#자리수(1)   0  1  1  1  1  1  1  1  1  1
#자리수(2)   1  1  2  2  2  2  2  2  2  1
#자리수(3)   1  3  3  4  4  4  4  4  3  2

dp = [[0 for i in range(10)] for j in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

sys.stdout.write("%d\n" % (sum(dp[N]) % 1000000000))

# for start in range(1, 10):
#     for i in range(1, N + 1):
#         for start in range(1, 10):
