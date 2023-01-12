import sys

N, M = map(int, sys.stdin.readline().split())

Nobj = set(map(int, sys.stdin.readline().split()))
Mobj = set(map(int, sys.stdin.readline().split()))

print(len(Nobj - Mobj) + len(Mobj - Nobj))
# print(Mobj - Nobj)
# print(Nobj)
# print(Mobj)

