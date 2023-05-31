from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    #맵 세팅
    cnt = 0
    N, M, K = map(int,input().split())
    graph = [[0] * M for _ in range(N)]

    for j in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    #배추 군집 찾기
    for a in range(N):
        for b in range(M):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)