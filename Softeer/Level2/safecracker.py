import sys

#그리드 알고리즘
capacity, n = map(int, sys.stdin.readline().split())
jams = []

for i in range(n):
    weight, price = map(int, sys.stdin.readline().strip().split())
    jams.append((weight, price))

#jams = sorted(jams, key=lambda x:(-x[1], x[0]))
jams = sorted(jams, key=lambda x: x[1], reverse=True)
result = 0
 

for jam in jams:
    if jam[0] <= capacity:
        capacity -= jam[0]
        result += jam[0] * jam[1]
    else:
        result += capacity * jam[1]
        break

print(result)


