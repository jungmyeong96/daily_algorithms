import sys
from collections import deque

def bfs(matureTomatos):
    stepX = [-1, 1, 0, 0]
    stepY = [0, 0, -1, 1]
    countRotate = 0
    countTomato = 0
    countDay = -1
    while matureTomatos:
        if countRotate == 0:
            countDay += 1
            countTomato = len(matureTomatos)
        X, Y = matureTomatos.popleft()

        for i in range(4):

            nx, ny = X + stepX[i], Y + stepY[i]
            if nx < 0 or ny < 0 or ny >= N or nx >= M:
                continue
            if tomatos[nx][ny] == 0:
                matureTomatos.append((nx, ny))
                tomatos[nx][ny] = 1
        countRotate += 1
        if countRotate == countTomato:
            countRotate = 0
    for i in range(M):
        if 0 in tomatos[i]:
            return -1
    return countDay

        

N, M = map(int, sys.stdin.readline().split())

tomatos = []
matureTomatos = deque()
count = 0

for i in range(M):
    tomatos.append(list(map(int, sys.stdin.readline().strip().split())))
    for j in range(N):
        if tomatos[i][j] == 1:
            matureTomatos.append((i, j))
print(bfs(matureTomatos))