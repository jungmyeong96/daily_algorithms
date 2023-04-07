from typing import List
import collections
import heapq

#다익스트라는 임의의 정점을 출발 집합에 더할 때, 그 정점까지의 최단거리는 계산이 끝났다는 확신을 갖고 더해야함
#무조건 최단 거리 기준 순회

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    graph = collections.defaultdict(list)
    #그래프 인접 구성
    #시작 정점을 키로 (도착, 소요시간) 값을 설정
    for u, v, w in times:
        graph[u].append((v, w))

    #큐 변수: [(소요시간, 정점)]
    Q = [(0, k)]
    dist = collections.defaultdict(int)

    #우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q) #최소 거리 기준으로 정렬됨.
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v)) 
    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == n:
        return max(dist.values())
    return -1

print(networkDelayTime([[3,1,5],[3, 2, 2],[2,1,2], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]], 8, 3))