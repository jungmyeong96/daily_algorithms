import sys

cnt = 0

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def dpFib(n):
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1

    for idx in range(3, n + 1):
        global cnt
        cnt += 1
        dp[idx] = dp[idx - 1] + dp[idx - 2]
    return dp[n]

n = int(sys.stdin.readline())

print(fib(n), cnt)