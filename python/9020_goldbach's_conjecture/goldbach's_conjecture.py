testcase = int(input())

def isPrime(num):
    for idx in range(2, num + 1):
        if num == idx:
            return True
        if num % idx == 0 :
            return False
    return False
        
    

while testcase != 0:
    target = int(input())
    #입력값은 무조건 짝수가 들어오니 target의 절반을 나눈다음 소수인지 검사한뒤 파티션을 증감해나감
    prime_one = prime_two = target // 2
    if isPrime(prime_one):
        print(f"{prime_one} {prime_two}")
    else:
        prime_one -= 1
        prime_two += 1
        while (isPrime(prime_one) == False or isPrime(prime_two) == False): #or이랑 | 이랑 다르다고??! |는 비트연산
            prime_one -= 1
            prime_two += 1
        print(f"{prime_one} {prime_two}")
    testcase -= 1