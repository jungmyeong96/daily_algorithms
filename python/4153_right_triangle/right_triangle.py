import sys

def func_pow(x):
    return pow(x, 2)

while 42:
    triangle = list(map(int, sys.stdin.readline().strip().split()))
    diagonal = max(triangle)
    if diagonal == 0:
        break
    triangle.remove(diagonal)
    calc = map(func_pow, triangle)
    if pow(diagonal, 2) == sum(calc):
        print("right")
    else:
        print("wrong")