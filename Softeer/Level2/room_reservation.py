import sys
import time
import collections

n, m = map(int, sys.stdin.readline().strip().split())

rooms = collections.defaultdict()

for _ in range(n):
    name = sys.stdin.readline().strip()
    rooms[name] = [0 for i in range(18)]

for _ in range(m):
    name, begin, end = (sys.stdin.readline().strip().split())
    for i in range(int(begin), int(end)):
        rooms[name][i] = -1

rooms = dict(sorted(rooms.items()))

keys = list(rooms.keys())
values = list(rooms.values())

for i in range(n):
    print("Room {}:".format(keys[i]))
    count = 0
    checker = 0
    for j in range(9, 18):
        if values[i][j] == 0 and checker == 0:
            checker = j
            count += 1
            values[i][j] = j + 1
        elif values[i][j] == 0 and checker != 0:
            values[i][checker] += 1
        elif values[i][j] == -1 and checker != 0:
            checker = 0
    values[i][0] = count
    if values[i][0] == 0:
        print("Not available")
    else:
        print("{} available:".format(values[i][0]))
    for j, room in enumerate(values[i][9:19]):
        if room != 0 and room != -1:
            print("{0:02d}-{1:d}".format(j + 9,room))
    if i != n - 1:
        print("-----")
    