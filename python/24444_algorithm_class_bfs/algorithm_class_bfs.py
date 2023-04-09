import sys
import collections
from collections import deque

def bfs(start):
    q = deque()
    visited[start] = 1
    q.append(start)
    cnt = 1
    result[start] = cnt
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                cnt += 1
                visited[i] = 1
                q.append(i)
                result[i] = cnt

N, M, R = map(int,sys.stdin.readline().split())

graph = collections.defaultdict(list)
visited = [0] * (N + 1)

for i in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(N + 1):
    graph[i].sort()

result = [0] * (N + 1)
bfs(R)

for i in result[1:]:
    print(i)