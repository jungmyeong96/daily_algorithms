import sys
# 시간초과

# N = int(input())


# xStack = []
# yStack = []
# xSlide = [] #x - y 같으면
# ySlide = [] #y + x 같으면

# count = 0

# def backTracking(startX, startY):
#     if len(xStack) == N:
#         global count
#         count += 1
#         # print(count)
#         # print("X:", end=" ")
#         # print(" ".join(map(str, xStack)))
#         # print("Y:", end=" ")
#         # print(" ".join(map(str, yStack)))
#         # chkecker = False
#         # for x in range(N):
#         #     for y in range(N):
#         #         chkecker = False
#         #         for idx in range(N):
#         #             if (x == xStack[idx]) and (y == yStack[idx]):
#         #                 print("x", end=" ")
#         #                 chkecker = True
#         #                 break
#         #         if chkecker == False:
#         #             print("0", end=" ")
#         #             chkecker=True
#         #     print("")
#         return
#     for x in range(startX, N):
#         for y in range(startY, N):
#             if (x in xStack) or (y in yStack) or ((x - y) in xSlide) or ((x + y) in ySlide) :
#                 continue
#             xStack.append(x)
#             yStack.append(y)
#             xSlide.append(x - y)
#             ySlide.append(x + y)
#             backTracking(startX + 1, startY)
#             xStack.pop()
#             yStack.pop()
#             xSlide.pop()
#             ySlide.pop()

# backTracking(0 , 0)
# print(count)


# # 0 0 x 0
# # x 0 0 0
# # 0 0 0 x
# # 0 x 0 0



N = int(sys.stdin.readline())

row = [0] * N
checked = [False for _ in range(N)] #열에 대한 체크
xSlide = [] #x - y 같으면
ySlide = [] #y + x 같으면

count = 0

def is_promising(x):
    for idx in range(x):
        if row[x] == row[idx] or abs(row[x] - row[idx]) == abs(x - idx):
            return False
    return True

def backTracking(startX):
    if startX == N:
        global count
        count += 1
        return
    for y in range(N):
        if checked[y] or ((startX - y) in xSlide) or ((startX + y) in ySlide):
            continue
        row[startX] = y
        if is_promising(startX) :
            checked[y] = True
            xSlide.append(startX - y)
            ySlide.append(startX + y)
            backTracking(startX + 1)
            checked[y] = False
            xSlide.pop()
            ySlide.pop()
        

backTracking(0)

sys.stdout.write("%d\n" % count)


# 0 0 x 0
# x 0 0 0
# 0 0 0 x
# 0 x 0 0
