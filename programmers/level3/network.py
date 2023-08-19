def solution(n, computers):
    answer = 0
    visited = []
    
    def dfs(i, computer, computers):
        if i in visited:
            return False
        visited.append(i)
        for idx, node in enumerate(computer):
            if node == 1:
                dfs(idx, computers[idx], computers)
        return True
        
    for i, computer in enumerate(computers):    
        if dfs(i, computer, computers):
            answer += 1
        
    return answer