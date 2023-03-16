from collections import deque
import sys

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while queue:
        maxNum = max(queue)
        target = queue.popleft()
        M -= 1
        if target == maxNum:
            count += 1
            if M < 0:
                sys.stdout.write("%d\n" %count)
                break
        else:
            queue.append(target)
            if M < 0:
                M = len(queue) - 1 #방금 삽입한 값이 타겟


    