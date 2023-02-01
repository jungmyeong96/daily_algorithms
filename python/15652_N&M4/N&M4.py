N, M = map(int,input().split())

stack = []

def backTracking(start):
    if len(stack) == M:
        print(" ".join(map(str, stack)))
        return
    for num in range(start, N + 1):
        # if len(stack) == 0 or (len(stack) != 0 and num >= stack[-1]):
            stack.append(num)
            backTracking(num)
            stack.pop()

backTracking(1)