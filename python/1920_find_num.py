
#1. 자료형으로 풀기
# import sys

# N = sys.stdin.readline()

# nNums = set(map(int, sys.stdin.readline().split()))

# M = sys.stdin.readline()

# mNums = list(map(int, sys.stdin.readline().split()))

# for num in mNums:
#     print(1) if num in nNums else print(0)

#2. 이분탐색으로 풀기
from sys import stdin, stdout
n = stdin.readline()
nNums = sorted(list((map(int,stdin.readline().split()))))
m = stdin.readline()
mNums = list(map(int, stdin.readline().split()))
print(mNums)

def binary(l, nNums, start, end):
    if start > end:
        return 0
    idx = (start+end)//2
    if l == nNums[idx]:
        return 1
    elif l < nNums[idx]:
        return binary(l, nNums, start, idx-1)
    else:
        return binary(l, nNums, idx+1, end)

for l in mNums:
    start = 0
    end = len(nNums)-1
    print(binary(l,nNums,start,end))