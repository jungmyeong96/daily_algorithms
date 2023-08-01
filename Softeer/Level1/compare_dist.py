import sys

# 주행거리 비교
# A, B 자연수 파라미터

a, b = map(int, sys.stdin.readline().split())

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("same")