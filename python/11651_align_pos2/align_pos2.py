
count = int(input())

array = [[0] * 2 for _ in range(count)]

for idx in range(count):
    array[idx] = list(map(int, input().split()))

array.sort(key = lambda x : (x[1], x[0]))

for idx in range(count):
    print(array[idx][0], array[idx][1])