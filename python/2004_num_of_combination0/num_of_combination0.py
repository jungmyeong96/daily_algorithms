

def factorial(num):
    result = 1
    for idx in range(1, num + 1):
        result *= idx
    return result

#특정 값중 해당 값이 몇개나 있는지 체크
def count_exponent(target, mantissa):
    result = 0
    while target > 0:
        target = target // mantissa
        result += target
    return result


N, M = map(int, input().split())
#지수의 차 개념으로 2와 5중 작은 값이 0의 개수
print(min((count_exponent(N, 2) - count_exponent(M, 2) - count_exponent(N - M, 2)), (count_exponent(N, 5) - count_exponent(M, 5) - count_exponent(N - M, 5))))

# combi = factorial(N) // (factorial(N - M) * factorial(M)) # 너무 오래걸림



# print(combi)