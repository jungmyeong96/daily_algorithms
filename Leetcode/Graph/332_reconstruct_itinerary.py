from typing import List
import collections
def findItinerary(tickets: List[List[str]]) -> List[str]:
    # 1. DFS로 일정 그래프 구성
    # # key와 value를 구분
    # graph = collections.defaultdict(list)
    # # 그래프 순서대로 구성
    # for a, b in sorted(tickets):
    #     graph[a].append(b)
    
    # route = []
    # def dfs(city: str):
    #     #첫 번째 값을 읽고 어휘순으로 방문합니다
    #     while graph[city]:
    #         dfs(graph[city].pop(0))
    #     route.append(city)

    # dfs('JFK')
    # #다시 뒤집어서 어휘 순서를 바꿔줌
    # return route[::-1]

    # 2. DFS로 일정 그래프 구성 (속도개선)
    # graph = collections.defaultdict(list)
    # for a, b in sorted(tickets, reverse=True):
    #     graph[a].append(b)
    
    # route = []
    # def dfs(city: str):
    #     while graph[city]:
    #         dfs(graph[city].pop())
    #     route.append(city)
    # dfs('JFK')
    # return route[::-1]
    
    #3. stack으로 풀어내기

    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)
    
    route, stack = [],["JFK"]
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())
    return route[::-1]

print(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))