import sys

n, m = map(int, sys.stdin.readline().split())

standard = [0]
check_speed = [0]

for _ in range(n):
    meter, speed = map(int, sys.stdin.readline().split())
    for i in range(1, meter + 1):
        standard.append(speed)


for _ in range(m):
    meter, speed = map(int, sys.stdin.readline().split())
    for i in range(1, meter + 1):
        check_speed.append(speed)

max_gap = 0
for i in range(101):
    max_gap = max(max_gap, check_speed[i] - standard[i])
print(max_gap)