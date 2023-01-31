n,m = list(map(int,input().split()))

stack = []

# def dfs():
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return
#     for i in range(1,n+1):
#         if i not in s:
#             s.append(i)
#             dfs()
#             s.pop()
 
# dfs()
 

def backTracking():
    if (len(stack) == m):
        print(' '.join(map(str, stack)))
        return
    for i in range(1, n + 1):
        if i not in stack:
            stack.append(i)
            backTracking()
            stack.pop()


backTracking()