import sys

n = int(sys.stdin.readline())

# triangle = [int(sys.stdin.readline())]
# jdx = 0

# for i in range(1, n):
#     line = list(map(int, sys.stdin.readline().strip().split()))
#     print(line)
#     if line[jdx] > line[jdx + 1]:
#         triangle[i] = line[jdx]
#     else:
#         triangle[i] = line[jdx + 1]
#         jdx += 1

# print(triangle[n - 1])
    

t = []
for i in range(n):
    t.append(list(map(int, sys.stdin.readline().split())))

k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            t[i][j] = t[i][j] + t[i - 1][j]
        elif i == j:
            t[i][j] = t[i][j] + t[i - 1][j - 1]
        else:
            t[i][j] = max(t[i - 1][j - 1], t[i - 1][j]) + t[i][j]
    k += 1

print(max(t[n - 1]))