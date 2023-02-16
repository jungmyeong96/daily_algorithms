import sys

N = int(sys.stdin.readline())

for i in range(N):
    checkParen = sys.stdin.readline()
    stack = []
    checker = True
    for c in checkParen:
        if c == '(':
            stack.append(c)
        elif len(stack) == 0 and c == ")":
            sys.stdout.write("NO\n")
            checker = False
            break
        elif c == ")":
            stack.pop()
    if len(stack) != 0:
        sys.stdout.write("NO\n")
    elif checker and len(stack) == 0:
        sys.stdout.write("YES\n")