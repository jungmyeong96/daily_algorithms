
def binomial(n, k): #파스칼의 삼각형응용
    if k == 0 or n == k:
        return 1
    return binomial(n - 1, k - 1) + binomial(n - 1, k)

n, k = map(int,input().split())

print(binomial(n, k))