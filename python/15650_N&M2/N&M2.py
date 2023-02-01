N, M = map(int,input().split())

stack = []

def backTracking():
    if len(stack) == M:
        print(" ".join(map(str, stack)))
        return
    for num in range(1, N + 1):
        length = len(stack)
        if num not in stack:
            if length == 0:
                stack.append(num)
            elif num > stack[length - 1]:
                stack.append(num)
            else :
                continue
            backTracking()
            stack.pop()

backTracking()