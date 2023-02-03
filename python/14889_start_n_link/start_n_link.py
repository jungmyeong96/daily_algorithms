import sys

N = int(sys.stdin.readline())

squad = []
# team = []
# otherTeam = [] #굳이 이렇게 팀배열을 나누지 말고 아래와 같이 불리언으로 구분
visited = [False] * N

minNum = sys.maxsize

for _ in range(N):
    squad.append(list(map(int, sys.stdin.readline().strip().split())))

def checkTeamScore():
    teamSum = 0
    otherTeamSum = 0

    for idx in range(N):
        for jdx in range(idx + 1, N):
            if visited[idx] and visited[jdx]:
                teamSum += squad[idx][jdx] + squad[jdx][idx]
            elif not visited[idx] and not visited[jdx]:
                otherTeamSum += squad[idx][jdx] + squad[jdx][idx]
    
    return abs(teamSum - otherTeamSum)

def dfs(depth, start):
    if depth == N // 2:
        score = checkTeamScore()
        global minNum
        if score < minNum:
            minNum = score
        return
    for player in range(start, N):
        if visited[0] == True: #대단한 발상! 코드를 짜면서 한 팀을 구하면 상대팀은 자동으로 결정되어 그 상대팀은 볼 필요가 없는데, 어떻게 해결할지 고민 중에
            return                  #숫자 하나를 특정해서 그 숫자에 해당되는 팀이 아니면 구하지 않는 방식으로 탐색횟수를 절반으로 줄일 수 
        visited[player] = True
        dfs(depth + 1, player + 1)
        visited[player] = False
dfs(0, 0)
sys.stdout.write("%d\n" % minNum)
