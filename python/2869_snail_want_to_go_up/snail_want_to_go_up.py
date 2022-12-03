import math

targets = list(map(int, input().split()))

# 시간초과

# days = 0
# height = 0

# while 42:
#     days += 1
#     height += targets[0]
#     if height >= targets[2]:
#         print(days)
#         break
#     height -= targets[1]

if (targets[0] >= targets[2]):
    print(1)
else :
    withoutLastday = targets[2] - targets[0]
    dayHeight = targets[0] - targets[1]
    takingTime = withoutLastday / dayHeight
    print(math.ceil(takingTime + 1))