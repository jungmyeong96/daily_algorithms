import sys

N = int(sys.stdin.readline())

# wires = [0] * (501)
# dp = [0] * 501

# for i in range(N):
#     A, B = map(int, sys.stdin.readline().split())
#     wires[A] = B

# for i in range(501):
#     if wires[i] == 0:
#         continue
#     dp[i] = 1
#     for j in range(i, 501):
#         if wires[j] == 0:
#             continue
#         if wires[j] > wires[i]:
#             dp[i] += 1


# for j in range(501):
#     if dp[j] != 0:
#         print("%d %d" % (j, dp[j]))
        
# print(N - max(dp))

wires = []
wires_b = []
dp = [0 for i in range(N)]
for i in range(N):
    wires.append(list(map(int, sys.stdin.readline().split())))
wires.sort(key = lambda x:x[0])
for i in range(N):
    wires_b.append(wires[i][1])

for i in range(N):
    for j in range(i):
        if wires_b[i] > wires_b[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    dp[i] = max(1, dp[i])

print(N - max(dp))