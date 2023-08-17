def solution(n):
    answer = 0

    
    for i in range(n, 0, -1):
        sum_num = 0
        for j in range(i, 0, -1):
            sum_num += j
            if sum_num > n:
                break
            elif sum_num == n:
                answer += 1
                i = i - 1
                break

        
    return answer