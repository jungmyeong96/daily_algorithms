from typing import List
import collections

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # DFS로 순환 구조 탐색
    graph = collections.defaultdict(list)
    #그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)
    
    traced = set()
    # 방문 노드 체크해서 배제하면 속도향상 (가지치기)
    visited = set()
    
    def dfs(i):
        #순환 구조이면 False
        if i in traced:
            return False
        #이미 방문했던 노드이면 False
        if i in visited:
            return True
        
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        #탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        #탐색 종료 후 방문 노드 추가
        visited.add(i)

        return True
    
    #키 값 기준 순환 구조 판별
    #list()를 써줌으로 아래 에러 방지
    #RuntimeError: dictionary changed size during iteration
    for x in list(graph):
        if not dfs(x):
            return False
    
    return True

print(canFinish(2, [[0, 1],[1, 0]]))