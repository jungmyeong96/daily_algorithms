import sys
from collections import deque

def bfs(init_pos_x, init_pos_y, dest_pos_x, dest_pos_y):
    q = deque()
    q.append([init_pos_x, init_pos_y])
    while q:
        x, y = q.popleft()
        if x == dest_pos_x and y == dest_pos_y:
            return board[dest_pos_x][dest_pos_y]
        for i in range(8):
            nx = x + step_x[i]
            ny = y + step_y[i]
            if 0 <= nx < board_size and 0 <= ny < board_size and board[nx][ny] == 0:
                q.append([nx, ny])
                board[nx][ny] = board[x][y] + 1    


step_x = [-1, -2, -2, -1, 1, 2, 2, 1]
step_y = [2, 1, -1, -2, -2, -1, 1, 2]

N = int(sys.stdin.readline())

for i in range(N):
    board_size = int(sys.stdin.readline())
    init_pos_x, init_pos_y = map(int, (sys.stdin.readline().split()))
    dest_pos_x, dest_pos_y = map(int, (sys.stdin.readline().split()))
    board = [[0] * board_size for _ in range(board_size)]
    print(bfs(init_pos_x, init_pos_y, dest_pos_x, dest_pos_y))
