num = int(input())

targets = list(map(int, input().split()))
count = 0
for idx in range(num):
    for target in range(2, targets[idx] + 1):
        if (target == targets[idx]): #자신이면 + 
            count += 1
        if (targets[idx] % target == 0): # 자신의 값이 나오기전 나눠지면 다음 수 체크
            break
print(count)