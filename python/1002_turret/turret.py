import math

count = int(input())

for _ in range(count):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if r1 > r2 :
        rr = r1 - r2
    else:
        rr = r2 - r1
    if (dist == 0) & (r1 == r2):
        print(-1)
    elif (dist == (r1 + r2))| (dist == rr):
        print(1)
    elif r1 + r2 > dist > rr :
        print(2)
    else:
        print(0)