import sys

count = int(sys.stdin.readline())

data = [[] for _ in range(count)]

for idx in range(count):
    data[idx] = list(sys.stdin.readline().strip().split())

data.sort(key=lambda x: int(x[0]))

for idx in range(count):
    sys.stdout.write("%s %s\n" % (data[idx][0], data[idx][1]))