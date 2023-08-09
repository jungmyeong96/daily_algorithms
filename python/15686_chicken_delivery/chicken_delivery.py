import sys

N, M = map(int, sys.stdin.readline().strip().split())

city_map = []

#조합은 백트래킹 DFS다~~
for i in range(N):
    city_map.append(list(map(int, sys.stdin.readline().strip().split())))

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if city_map[i][j] == 1:
            house.append([i, j])
        elif city_map[i][j] == 2:
            chicken.append([i, j])

stack = []
min_dist = float('inf')

def backtracking(idx):
    global min_dist
    if len(stack) == M:
        whole_dist = 0
        for h in house:
            dist = 999999
            for c in chicken:
                dist = min(dist, abs(c[0] - h[0]) + abs(c[1] - h[1]))
            whole_dist += dist
        min_dist = min(whole_dist, min_dist)
        return

    for i in range(idx, len(chicken)):
        if chicken[i] not in stack:
            stack.append(chicken[i])
            backtracking(i + 1)
            stack.pop()
    return
            
backtracking(0)
print(min_dist)


