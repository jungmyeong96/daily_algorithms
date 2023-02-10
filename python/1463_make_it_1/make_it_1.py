import sys
#배열에 해당 수까지의 답을 담아가는 동적프로그래밍

#Bottom up

N = int(sys.stdin.readline())

# counts = [0] * (N + 1)

# for i in range(2, N + 1):
#     counts[i] = counts[i - 1] + 1
#     if i % 2 == 0:
#         counts[i] = min(counts[i], counts[i // 2] + 1)
#     if i % 3 == 0:
#         counts[i] = min(counts[i], counts[i // 3] + 1)

# sys.stdout.write("%d\n" % counts[N])


#Top down

dp = {1:0}

def rec(n):
    if n in dp.keys():
        return dp[n]
    if (n % 3 == 0) and (n % 2 == 0):
        dp[n] = min(rec(n//3)+1, rec(n//2) + 1)
    elif n%3 == 0:
        dp[n] = min(rec(n//3) + 1, rec(n-1) + 1)
    elif n%2 == 0:
        dp[n] = min(rec(n//2) + 1, rec(n-1) + 1)
    else:
        dp[n] = rec(n-1) + 1
    return dp[n]
sys.stdout.write("%d\n" % rec(n))