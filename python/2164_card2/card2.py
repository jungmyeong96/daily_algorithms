import sys
from collections import deque

cards = deque()

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    cards.append(i)

rules = 1

while 42:
    if len(cards) == 1:
        sys.stdout.write(f'{cards[0]}\n')
        break
    if rules % 2 == 1:
        cards.popleft()
    else:
        cards.append(cards[0])
        cards.popleft()
    rules += 1
