count = int(input())
number = list(map(int, input().split()))
target = int(input())
result = 0
for num in number:
    if target == num:
        result += 1
print(result)