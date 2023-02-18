import sys

N = int(sys.stdin.readline())

waitlist = list(map(int,sys.stdin.readline().split()))

waitlist.sort()

for i in range(1, N):
    waitlist[i] = waitlist[i - 1] + waitlist[i]

sys.stdout.write(f'{sum(waitlist)}')