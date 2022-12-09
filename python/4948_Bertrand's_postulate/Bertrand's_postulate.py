import math

while 42:
    target = int(input())
    if target == 0:
        break
    arr = [0 for _ in range((target * 2) + 1)]
    arr[1] = 1
    for check in range(2, int(math.sqrt(target * 2)) + 1):
        if (arr[check] == 0):
            idx = 2
            while check * idx <= (target * 2):
                arr[check * idx] = 1
                idx += 1
    count = 0
    for idx in range(target + 1, (target * 2) + 1):
        if arr[idx] == 0:
            count += 1
    print(count)