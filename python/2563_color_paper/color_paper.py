count = int(input())
result = 0

arr = [[0] * 101 for _ in range(101)]
result = 0

for _ in range(count):
    x, y = map(int, input().split())
    for pos_y in range(y, y + 10):
        for pos_x in range(x, x + 10):
            arr[pos_y][pos_x] = 1
for pos_y in range(101):
    for pos_x in range(101):
        if arr[pos_y][pos_x] == 1:
            result += 1

print(result)

