def solution(A,B):
    answer = 0

    whole_len = len(A)
    
    A.sort()
    B.sort(reverse=True)
    
    for i in range(whole_len):
        answer += A[i] * B[i]
        
    return answer