import sys
from collections import Counter

testcase = int(sys.stdin.readline())

#서로 다른 주머니에서 경우의수 파악

#(n + 1) * (m + 1) ... - 1

# for _ in range(testcase):
#     numOfClothes = int(sys.stdin.readline())
#     clothes = {}
#     for idx in range(numOfClothes):
#         cloth, typeOfCloth = sys.stdin.readline().split()
#         if typeOfCloth in clothes:
#             clothes[typeOfCloth].append(cloth)
#         else:
#             clothes[typeOfCloth] = [cloth]
#     cnt = 1
#     for idx in clothes:
#         cnt *= len(clothes[idx]) + 1
#     sys.stdout.write("%d\n" % (cnt - 1))


for _ in range(testcase):
    numOfClothes = int(sys.stdin.readline())
    clothes = []
    for idx in range(numOfClothes):
        cloth, typeOfCloth = sys.stdin.readline().split()
        clothes.append(typeOfCloth)   
    numOfType = Counter(clothes)
    cnt = 1
    for idx in numOfType:
        cnt *= numOfType[idx] + 1
    sys.stdout.write("%d\n" % (cnt - 1))
