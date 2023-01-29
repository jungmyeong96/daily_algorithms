import sys
from itertools import combinations

testcase = int(sys.stdin.readline())

# for _ in range(testcase):
#     combi = []
#     N, M = map(int, sys.stdin.readline().split())
#     for idx in range(M):
#         combi.append(idx)
#     if N == M:
#         sys.stdout.write("1\n")
#     else:
#         countList = list(combinations(combi, N))
#         print(countList)
#         sys.stdout.write("%d\n" % len(countList))


# 조합으로 푸는 문제 nCm  =  N! // ((N - M)! * M!)


def factorial(num):
    result = 1
    for idx in range(1, num + 1):
        result *= idx
    return result

for _ in range(testcase):
    N, M = map(int, sys.stdin.readline().split())
    sys.stdout.write("%d\n" % (factorial(M) // (factorial(M - N) * factorial(N))))
