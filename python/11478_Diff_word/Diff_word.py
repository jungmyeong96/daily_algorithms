import sys

word = sys.stdin.readline().strip()

ans = set()

for i in range(len(word)):
    for j in range(i, len(word)):
        ans.add(word[i:j + 1])
print(len(ans))