import sys
import time



N,K = map(int, sys.stdin.readline().strip().split())


nums = list(map(int, sys.stdin.readline().strip().split()))

maxNum = -100000000000
# start = time.time()
sumNum = 0
for i in range((N - (K - 1))):
    if maxNum == -100000000000:
        for j in range(i, i + K):
            sumNum += nums[j]
    else:
        sumNum -= nums[i - 1]
        sumNum += nums[i + K - 1]
    if sumNum > maxNum:
        maxNum = sumNum

# end = time.time()
# sys.stdout.write("%.5f sec" % (end - start))
sys.stdout.write("%d\n" % maxNum)