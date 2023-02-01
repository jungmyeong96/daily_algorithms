N, M = map(int, input().split())

stack = []

def backTracking():
    if len(stack) == M:
        print(" ".join(map(str, stack)))
        return
    for num in range(1, N + 1):
        stack.append(num)
        backTracking()
        stack.pop()

backTracking()