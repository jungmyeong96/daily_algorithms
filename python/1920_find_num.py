import sys

N = sys.stdin.readline()

nNums = set(map(int, sys.stdin.readline().split()))

M = sys.stdin.readline()

mNums = list(map(int, sys.stdin.readline().split()))

for num in mNums:
    print(1) if num in nNums else print(0)
