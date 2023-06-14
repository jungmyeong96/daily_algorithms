import sys

N = int(sys.stdin.readline())

company = {}

for _ in range(N):
    name, action = sys.stdin.readline().strip().split()
    if action == "enter":
        company[name] = action
    elif action == "leave":
        del company[name]

for person in sorted(company, reverse=True):
    print(person)