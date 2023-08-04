import sys
from collections import deque

# 많은 개수의 학생
# 많은 개수의 케이스

n, k = map(int, sys.stdin.readline().split())

students = list((map(int, sys.stdin.readline().split())))

for i in range(k):
    begin, end = map(int, sys.stdin.readline().split())
    sum_num = 0
    avg_num = 0
    for j in range(begin - 1, end):
        sum_num += students[j]
    avg_num = sum_num / (end - begin + 1)
    print("{0:.2f}".format(avg_num))

