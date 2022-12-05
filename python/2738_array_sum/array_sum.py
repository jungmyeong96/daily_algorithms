N ,M = map(int, input().split())

array = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]

for i in range(2):
    for j in range(N):
        array[i][j] = list(map(int, input().split()))

for y in range(N):
    for x in range(M):
        print(array[0][y][x] + array[1][y][x], end="")
        if (x == M - 1):
            print('\n', end="")
        else:
            print(' ', end="")
