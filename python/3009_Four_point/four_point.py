# import sys

# x1, y1 = map(int, sys.stdin.readline().split())
# x2, y2 = map(int, sys.stdin.readline().split())
# x3, y3 = map(int, sys.stdin.readline().split())

# if x1 == x2:
#     x4 = x3
# elif x1 == x3:
#     x4 = x2
# else:
#     x4 = x1

# if y1 == y2:
#     y4 = y3
# elif y1 == y3:
#     y4 = y2
# else:
#     y4 = y1

# # sys.stdout.write(str(x4) + " " + str(y4))
# print("%d %d" % (x4, y4))

x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print("%d %d" % (x4, y4))