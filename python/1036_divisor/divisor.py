import sys

testcase = int(sys.stdin.readline())

numbers = list(map(int,sys.stdin.readline().split()))

# maxNum = max(numbers) * 2

numbers.sort(reverse=True)

#시간초과
# while 42:
#     checker = True
#     for idx in range(testcase):
#         if maxNum % numbers[idx] != 0:
#             checker = False
#             break
#     if checker == True:
#         break

#sys.stdout.write("%d" % maxNum)

sys.stdout.write("%d" % (numbers[0] * numbers[-1]))

