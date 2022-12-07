minNum = int(input())
maxNum = int(input())

mini = result = 0
for num in range(minNum, maxNum + 1):
    if num == 1:
        continue
    for idx in range(2, num + 1):
        if (num == idx):
            result += num
            if (mini == 0):
                mini = num
        if (num % idx == 0):
            break
if (result == 0):
    print(-1)
else:
    print(result)
    print(mini)