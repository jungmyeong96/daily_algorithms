import sys

N, M = map(int, sys.stdin.readline().split())

checker = {}
for _ in range(N):
    checker[sys.stdin.readline().strip()] = 0

for _ in range(M):
    word = sys.stdin.readline().strip()
    if  word in checker:
        checker[word] = checker[word] + 1

print(sum(checker.values()))
