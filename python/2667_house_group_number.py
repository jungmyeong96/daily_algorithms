import sys
from typing import List
from collections import Counter

def dfs(group_house: List[List[int]], i: int, j: int, num: int):
    if i < 0 or j < 0 or i >= N or j >= N or group_house[i][j] == 0 or visited[i][j] == 1:
        return
    visited[i][j] = 1
    group_house[i][j] += num
    dfs(group_house, i + 1, j, num)
    dfs(group_house, i - 1, j, num)
    dfs(group_house, i, j + 1, num)
    dfs(group_house, i, j - 1, num)
    

N = int(sys.stdin.readline())

if N == 0:
    print(0)

group_house = [[] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
   houses = sys.stdin.readline()
   for j in range(N):
    group_house[i].append(int(houses[j]))

num = 0
for i in range(N):
    for j in range(N):
        if group_house[i][j] == 1 and visited[i][j] == 0:
            dfs(group_house, i, j, num)
            num += 1

ans = [data for houses in group_house for data in houses]

counter = Counter(ans)
if 0 in counter:
    counter.pop(0)
sys.stdout.write("%d\n" %len(counter)) 
count_ans = list(counter.values())
# print(count_ans)
count_ans.sort()
for i in range(len(count_ans)):
    print(count_ans[i])
# for i in range(len(counter)):
#     sys.stdout.write("%d\n" %counter[i + 1])
# for i in range(N):
#     print(group_house[i])