import sys
import heapq


n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, (-x, x)) #우선순위 큐를 이용해 최대힙만들기
    else:
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1])
        else:
            print(0)