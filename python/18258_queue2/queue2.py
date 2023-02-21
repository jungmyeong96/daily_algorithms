import sys
from collections import deque

N = int(sys.stdin.readline())

# queue = list()

# for i in range(N):
#     orders = list(sys.stdin.readline().strip().split())
#     if orders[0] == "push":
#         queue.append(orders[1]) #O(1)
#     elif orders[0] == "pop":
#         if len(queue) == 0: #O(1)
#             sys.stdout.write("-1\n")
#         else:
#             sys.stdout.write(f'{queue[0]}\n')
#             queue.pop(0) #O(n)
#     elif orders[0] == "front":
#         if len(queue) == 0: #O(1)
#             sys.stdout.write("-1\n")
#         else:
#             sys.stdout.write(f'{queue[0]}\n') #O(1)
#     elif orders[0] == "back":
#         if len(queue) == 0: #O(1)
#             sys.stdout.write("-1\n")
#         else:
#             sys.stdout.write(f'{queue[-1]}\n') #O(1)
#     elif orders[0] == "size":
#         sys.stdout.write(f'{len(queue)}\n') #O(1)
#     elif orders[0] == "empty":
#         if len(queue) == 0: #O(1)
#             sys.stdout.write("1\n")
#         else:
#             sys.stdout.write("0\n")

## pop(0)에서 시간초과

q = deque([])
for i in range(N):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        q.append(s[1])
    elif s[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft()) #O(1)에 가능
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif s[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])