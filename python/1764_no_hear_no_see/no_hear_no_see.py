import sys

N, M = map(int, sys.stdin.readline().split())

noHear = []

noSee = []

for i in range(N):
    noHear.append(sys.stdin.readline().strip())

for i in range(M):
    noSee.append(sys.stdin.readline().strip())

noHearNoSee = sorted(list(set(noHear) & set(noSee)))

noHSlen = len(noHearNoSee)
sys.stdout.write("%d\n" % noHSlen)
for i in range(noHSlen):
    sys.stdout.write("%s\n" % noHearNoSee[i])