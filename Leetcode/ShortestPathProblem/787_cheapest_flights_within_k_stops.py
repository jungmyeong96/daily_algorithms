from typing import List
import collections
import heapq

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = collections.defaultdict(list)
    # 그래프 인접리스트를 구성합니다.
    for u, v, w in flights:
        graph[u].append((v, w))
    
    # 우선순위큐
    Q = [(0, src, k + 1)]
    check = collections.defaultdict()

    # 최소 비용으로 도착점까지 가는 비용 책정
    while Q:
        price, node, trans_max = heapq.heappop(Q)
        if node == dst and trans_max >= 0:
            return price
        if trans_max >= 0 and (node not in check or trans_max >= check[node]):
            check[node] = trans_max
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, trans_max - 1))
    return -1

print(findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))