import sys


# local minimum이 발생하지 않는 조건

N, K = map(int, sys.stdin.readline().split())

kindOfCoin = []

for _ in range(N):
    coin = int(sys.stdin.readline().strip())
    if coin > K:
        break
    kindOfCoin.append(coin)

kindOfCoin.sort(reverse=True)

count = 0

for coin in kindOfCoin:
    maxCoin = K // coin
    if  maxCoin > 0:
        count += maxCoin
        K = K - (coin * maxCoin)
    if K == 0:
        break

print(count)
    
    