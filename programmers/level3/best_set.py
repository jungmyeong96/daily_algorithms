#없으면 -1
#오름차순
def solution(n, s):
    answer = []
    if s < n:
        answer.append(-1)
        return answer
    mod = s % n
    share = s // n
    for i in range(n):
        answer.append(share)
        if i >= n - mod:
            answer[i] += 1
    return answer