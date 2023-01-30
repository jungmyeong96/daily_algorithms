from fractions import Fraction

def gcd(x, y):
    if y == 0:
        return x
    else:
        return (y, x % y)

testcase = int(input())

rings = list(map(int, input().split()))

for idx in range(1, testcase):
    result = Fraction(rings[0], rings[idx])
    print("%d/%d"% (result.numerator, result.denominator))



