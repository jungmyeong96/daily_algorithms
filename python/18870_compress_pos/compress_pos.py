import sys

count = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))

sorted_data = sorted(list(set(data)))

# for idx in range(count):
#     sys.stdout.write("%d" % sorted_data.index(data[idx]))
#     if idx != count - 1:
#         sys.stdout.write(' ')

new_data = {}

for idx in range(len(sorted_data)):
    new_data[sorted_data[idx]] = idx

for idx in data:
    sys.stdout.write("%s " % new_data[idx])