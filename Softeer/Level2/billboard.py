import sys
import collections

list_num = [
    0b1101111,
    0b0000011,
    0b1011101,
    0b1010111,
    0b0110011,
    0b1110110,
    0b1111110,
    0b1100011,
    0b1111111,
    0b1110111,
]

def calc_diff(num1, num2):
    count = 0
    while num1 >= 1:
        b = num1 % 10
        a = num2 % 10
        changed = collections.Counter(format(list_num[b] ^ list_num[a], 'b'))
        count += changed['1']
        num1 //= 10
        num2 //= 10
    while num2 >= 1:
        a = num2 % 10
        changed = collections.Counter(format(0b0000000 ^ list_num[a], 'b'))
        count += changed['1']
        num2 //= 10
    return count

n = int(sys.stdin.readline())
count = 0

for _ in range(n):
    before, after = map(int, sys.stdin.readline().split())

    if before < after:
        count = calc_diff(before, after)
    else:
        count = calc_diff(after, before)
    print(count)




