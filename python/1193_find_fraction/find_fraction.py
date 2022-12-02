# 1 2 6 7 15 16
# 3 5 8 14 17
# 4 9 13 18
# 1012 19 25
# 11 20 24
# 21 23
# 22
target = int(input())

coor = 1

# 12 1
# 11 2
# 9 3
# 6 4
# 2 5

while target > coor:
    target -= coor
    coor += 1

if (coor % 2 == 0):
    top = target
    bottom = coor - target + 1
else :
    top = coor - target + 1
    bottom = target
script = f'{top}/{bottom}'
print (script)