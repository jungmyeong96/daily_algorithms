import sys
from typing import List

sys.setrecursionlimit(10**6)

def dfs(graph:  List[List[int]], visited:  List[int], R: int):
    global cnt
    visited[R] = cnt
    for i in graph[R]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, visited, i)
    return


cnt = 1
N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    U, V = map(int, sys.stdin.readline().split())
    graph[U].append(V)
    graph[V].append(U)

for i in range(1, N + 1):
    graph[i].sort(reverse=True)

dfs(graph, visited, R)

for i in range(1, N + 1):
    sys.stdout.write("%d\n" %visited[i])

