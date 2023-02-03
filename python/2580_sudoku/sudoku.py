# import sys

# sudoku = []
# answer = []

# isPrint = False

# for idx in range(9):
#     sudoku.append(list(map(int, sys.stdin.readline().strip().split())))


# def printAnswer():
#     for idx in range(9):
#         for jdx in range(9):
#             sys.stdout.write("%d " %answer[idx][jdx])

# def dfs(start):
#     if isPrint == True:
#         return
#     if len(answer) == 9:
#         printAnswer()
#         isPrint = True
#         return
#     answer[start] = sudoku[start]
#     if 0 not in sudoku[start]:
#         dfs(start + 1)
#         return
#     for num in range(9):
#         if sudoku[start][num] == 0:
#             newNum = checkNum()
#             if newNum == -1:
#                 return
#             answer[start][num] = newNum
#             dfs(start + 1)
#             answer[start][num] = 0

# dfs(0)



# dfs는 무조건 라인별이 아니고 찾고자 하는 위치값에 대한 경우니까 blank를 기준으로 두는게 맞음

import sys

sudoku = []
blank = []

isPrint = False

for idx in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().strip().split())))

for y in range(9):
    for x in range(9):
        if sudoku[y][x] == 0:
            blank.append((x, y))


def printAnswer():
    for idx in range(9):
        for jdx in range(9):
            sys.stdout.write("%d " %sudoku[idx][jdx])
        sys.stdout.write("\n")


def checkRow(num, y):
    for x in range(9):
        if num == sudoku[y][x]:
            return False
    return True

def checkCol(num, x):
    for y in range(9):
        if num == sudoku[y][x]:
            return False
    return True

def checkRect(num, x, y):
    i = x // 3 * 3
    j = y // 3 * 3
    for y in range(3):
        for x in range(3):
            if num == sudoku[j + y][i + x]:
                return False
    return True

def dfs(start):
    if len(blank) == start:
        printAnswer()
        exit(0)
    for num in range(1, 10):
        x = blank[start][0]
        y = blank[start][1]
        if checkCol(num, x) and checkRow(num, y) and checkRect(num, x, y):
            sudoku[y][x] = num
            dfs(start + 1)
            sudoku[y][x] = 0

dfs(0)