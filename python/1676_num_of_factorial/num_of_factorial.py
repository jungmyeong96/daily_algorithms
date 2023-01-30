import sys

# def factorial(num):
#     result = 1
#     for idx in range(1, num + 1):
#         result *= idx
#     return result

# num = int(sys.stdin.readline())
# ans = 0
# for idx in range(1, num + 1):
#     if (idx % 125 == 0):
#         ans += 1
#     if (idx % 25 == 0):
#         ans += 1
#     if (idx % 5 == 0):
#         ans += 1

n=int(input())

cnt=0
while n>0:
  cnt+=n//5
  n//=5

print(cnt)

# sys.stdout.write("%d\n" % ans)
#  = factorial(num)X
