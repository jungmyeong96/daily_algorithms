import sys

N = int(sys.stdin.readline())

meetingSchedul = []

for i in range(N):
    meetingSchedul.append(list(map(int, sys.stdin.readline().strip().split())))

# 종료의 시각이 가장 빠른 순대로 정렬
# 그 중, 시작 순서가 가장 빠른거 순대로 정렬

meetingSchedul.sort(key= lambda x:(x[1], x[0]))

end = meetingSchedul[0][1]

cnt = 1

for i in range(1, N):
    if meetingSchedul[i][0] >= end:
        cnt += 1
        end = meetingSchedul[i][1]

print(cnt)