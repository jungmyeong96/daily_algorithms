import sys
import heapq

N = int(sys.stdin.readline())

maze_map = []
sx = [0, 0, 1, -1]
sy = [-1, 1, 0, 0]

for i in range(N):
    maze_map.append(list(map(int,list(sys.stdin.readline().strip()))))

visited = [[0] * N for _ in range(N)]

def bfs():
    queue = []
    count = 0
    heapq.heappush(queue, [count, 0, 0])
    while heapq:
        count, cx, cy = map(int, heapq.heappop(queue))
        visited[cx][cy] = 1

        if (cx, cy) == (N - 1, N - 1):
            print(count)
            return

        for i in range(4):
            nx, ny = cx + sx[i], cy + sy[i]
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if maze_map[nx][ny] == 1:
                    heapq.heappush(queue, [count, nx, ny])
                else:
                    heapq.heappush(queue, [count + 1, nx, ny])
    return 

bfs()