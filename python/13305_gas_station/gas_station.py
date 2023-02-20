import sys

N = int(sys.stdin.readline())

distances =  list(map(int, sys.stdin.readline().strip().split()))

stations = list(map(int, sys.stdin.readline().strip().split()))

# stations.pop()

# minimumPrice = min(stations)

# totalCosts = 0
# for i in range(N - 1):
#     if stations[i] == minimumPrice:
#         wholeDistance = 0
#         for j in range(i, N - 1):
#             wholeDistance += distances[j]
#         totalCosts += stations[i] * wholeDistanceg
#         break
#     else:
#         totalCosts += stations[i] * distances[i]

# sys.stdout.write(f'{totalCosts}\n')

##위의 코드는 최소를 찾을 수가 없음 

totalCosts = distances[0] * stations[0]
minimumPrice = stations[0]

for i in range(1, N - 1):
    if stations[i] < minimumPrice:
        minimumPrice = stations[i]
    totalCosts += minimumPrice * distances[i]

sys.stdout.write(f'{totalCosts}\n')