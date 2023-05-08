from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int,input().split())
link = [[] for _ in range(N+1)]
visited = [0] * (N+1)
visited[R] = 1
cnt = 1
q = deque([R])

for _ in range(M):
    A, B = map(int,input().split())
    link[A].append(B)
    link[B].append(A)

for i in range(1,N+1):
    link[i].sort(reverse = True)

while q:
    v = q.popleft()
    for i in link[v]:
        # 큐에 새로 넣어줄 때 방문 여부를 체크한다.
        if visited[i]:
            continue
        cnt+=1
        visited[i] = cnt
        q.append(i)
print(*visited[1:], sep="\n")