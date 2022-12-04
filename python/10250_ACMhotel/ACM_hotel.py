testcase = int(input())

for i in range(testcase):
    h, w, n = map(int, input().split())
    floor = n % h
    cell = n // h + 1
    if floor == 0:
        cell -= 1
        floor = h
    print(floor * 100 + cell)
