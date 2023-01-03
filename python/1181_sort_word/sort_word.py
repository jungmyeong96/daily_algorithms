import sys

count = int(sys.stdin.readline())

data = []

for idx in range(count):
    data.append(sys.stdin.readline().strip())

nodup = list(set(data))

nodup.sort(key=lambda x: (len(x), x))

for idx in nodup:
    sys.stdout.write(idx)
    sys.stdout.write('\n')