import sys

N = int(sys.stdin.readline())

sequence = []
stack = []
ans = []

for i in range(N):
    sequence.append(int(sys.stdin.readline().strip()))

checker = 0

def stack_sequence():
    global checker
    checker = 0
    for num in sequence:
        if len(stack) != 0 and stack[-1] == num:
            stack.pop()
            ans.append("-")
            continue
        if checker < num:
            for i in range(checker + 1, num + 1):
                stack.append(i)
                checker += 1
                ans.append("+")
            if stack[-1] == num:
                stack.pop()
                ans.append("-")
        else:
            print("NO")
            return False
    return True


if stack_sequence():
    for a in ans:
        print(a)