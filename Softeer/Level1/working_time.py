import sys

#  계약시간 <= 총 근로 시간 < 법정 근로시간 초과 X 
# 근무시간 = 출근 ~ 퇴근
# 5일동안 총 몇분 근무

def calcWorkingTime() -> int:
    sum = 0
    for i in range(5):
        start, end = sys.stdin.readline().strip().split()
        start_hour, start_min = map(int, start.split(":"))
        end_hour, end_min = map(int, end.split(":"))
        end_time = end_hour * 60 + end_min
        start_time = start_hour * 60 + start_min
        sum += end_time - start_time
    return sum

print(calcWorkingTime())


