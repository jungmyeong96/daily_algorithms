import sys

# 투 포인터? 슬라이드 윈도우  

def secretManu():
    m, n, k = map(int, sys.stdin.readline().split())

    secret = list(map(int, sys.stdin.readline().strip().split()))

    nums = list(map(int, sys.stdin.readline().strip().split()))

    start = 0
    end = 0
    for start in range(n):
        i = 0
        end = start
        while end < start + m and end < n:
            if nums[end] != secret[i]:
                break
            end += 1
            i += 1

        if end - start == m:
            print("secret")
            return

    print("normal")

secretManu()





# import sys
# input = sys.stdin.readline 

# m,n,k = map(int,input().split())

# if m > n :
#     print("normal")
#     exit()

# secret_key = "".join(list(map(str,input().split())))
# user_input = "".join(list(map(str,input().split())))

# if secret_key in user_input:
#     print("secret")
# else:
#     print("normal")