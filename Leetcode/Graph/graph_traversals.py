
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

#1. DFS 재귀
# 사전식 순서로 탐색 [1, 2, 5, 6, 7, 3, 4]
# 제약 충족 문제에서 백트래킹으로 자주 사용
def recusive_dfs(v, discovered = []):
    #저장 경로
    discovered.append(v)
    #순회 경로
    for w in graph[v]:
        if w not in discovered: # 새로운 경로 탐색
            discovered = recusive_dfs(w, discovered)
    return discovered

#2. DFS STACK
#역순으로 탐색 [1, 4, 3, 5, 7, 6, 2]
#직관적이고 속도가 더 빠름
def iterative_dfs(start_v):
    #저장 경로
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

#3. BFS QUEUE
# 너비 우선 탐색 [1, 2, 3, 4, 5, 6, 7]
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

print(recusive_dfs(1))
print(iterative_dfs(1))
print(iterative_bfs(1))