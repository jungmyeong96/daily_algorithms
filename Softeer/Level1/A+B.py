import sys

# TC , 입력정수 A B
def sumNum():
    tc = int(sys.stdin.readline())
    for i in range(1, tc + 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        print("Case #{0}: {1}".format(i, a+b))

sumNum()