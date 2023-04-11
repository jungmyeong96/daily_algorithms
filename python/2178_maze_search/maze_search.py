import sys
from collections import deque

def bfs(x: int, y: int):
    stepX = [-1, 1, 0, 0]
    stepY = [0, 0, -1, 1]

    path = deque()
    path.append((x, y))

    while path:
        x, y = path.popleft()

        for i in range(4):
            nx = x + stepX[i]
            ny = y + stepY[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            # print(nx, ny)
            # print(maze)
            if maze[nx][ny] == 0:
                continue
                
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                path.append((nx, ny))

    return maze[N - 1][M - 1]

N, M = map(int, sys.stdin.readline().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip())))

print(bfs(0, 0))