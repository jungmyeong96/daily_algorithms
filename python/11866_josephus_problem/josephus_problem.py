import sys
from collections import deque

people = deque()

N, K = map(int,sys.stdin.readline().strip().split())


for i in range(1, N+1):
    people.append(i)

deadBody = []

# target = K - 1

# while len(people) >= K:
#     deadBody.append(people.pop(target))
#     target = (target + K - 1) % (len(people))

# if len(people) < K:
#     while people:
#         deadBody.append(people.pop(0))


while people:
    for i in range(K-1):
        people.append(people.popleft())
    deadBody.append(people.popleft())


sys.stdout.write("<")
for i in range(len(deadBody)):
    sys.stdout.write(f'{deadBody[i]}')
    if i != len(deadBody) - 1:
        sys.stdout.write(", ")
sys.stdout.write(">")
