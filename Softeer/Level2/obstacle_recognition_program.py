import sys

def dfs(x, y) -> bool:
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if swmap[x][y] == 1:
        swmap[x][y] = 0
        checkmap.append(1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

n = int(sys.stdin.readline())

swmap = []
checkmap = []
result = []
count = 0

for i in range(n):
    line = list(map(int, sys.stdin.readline().strip()))
    swmap.append(line)

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            result.append(len(checkmap))
            checkmap = []
            count += 1

print(count)
result.sort()
for r in result:
    print(r)