target = int(input())

ans = 0
while target >= 0: #5로 나눈 몫이 최소연산인것을 알기 때문에 5로 나눈 몫이 0인지 지속적으로 검사하며 3을 뺌
    if target % 5 == 0:
       ans += target // 5
       print(ans)
       break
    target -= 3
    ans += 1
if target < 0:
    print(-1)