import sys
import math

testcase = int(sys.stdin.readline())

for _ in range(testcase):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    planet_count = int(sys.stdin.readline())
    planet_route = 0
    for idx in range(planet_count):
        cx, cy, r = map(int, sys.stdin.readline().strip().split())
        if (((math.sqrt((cx - x1) ** 2 + (cy - y1) ** 2) <= r) and (math.sqrt((cx - x2) ** 2 + (cy - y2) ** 2) > r)) or
        ((math.sqrt((cx - x1) ** 2 + (cy - y1) ** 2) > r) and (math.sqrt((cx - x2) ** 2 + (cy - y2) ** 2) <= r))):
            planet_route += 1
    sys.stdout.write("%d\n" % planet_route)
    