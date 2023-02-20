import sys

N = int(sys.stdin.readline())

meetingSchedule = []

for i in range(N):
    meetingSchedule.append(list(map(int, sys.stdin.readline().strip().split())))

# 종료의 시각이 가장 빠른 순대로 정렬
# 그 중, 시작 순서가 가장 빠른거 순대로 정렬

meetingSchedule.sort(key= lambda x:(x[1], x[0]))

end = meetingSchedule[0][1]

cnt = 1

for i in range(1, N):
    if meetingSchedule[i][0] >= end:
        cnt += 1
        end = meetingSchedule[i][1]

print(cnt)