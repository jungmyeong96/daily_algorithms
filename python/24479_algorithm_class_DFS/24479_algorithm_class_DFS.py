
import sys

sys.setrecursionlimit(10**6)

def dfs(graph, visit, R):
    global cnt
    visit[R] = cnt
    
    for i in graph[R]:  
        if visit[i] == 0:
            cnt += 1
            
            dfs(graph, visit, i)

N, M, R= map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
cnt = 1

for i in range(M):
    U, V = map(int, sys.stdin.readline().strip().split())
    graph[U].append(V)
    graph[V].append(U)

#graph.sort()
for i in range(N+1):
    graph[i].sort()

dfs(graph, visit, R)

for idx in range(1, N + 1):
    sys.stdout.write("%d\n" %visit[idx])

