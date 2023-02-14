import sys


N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

dp1 = [1] * N
dp2 = [1] * N

sub_len = [0] * N

Max = 0
#1 5 2 1 4 3 4 5 2 1
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

nums.reverse()

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

dp2.reverse()

for i in range(N):
    sub_len[i]=dp1[i]+dp2[i]

sys.stdout.write("%d\n" % (max(sub_len) - 1))