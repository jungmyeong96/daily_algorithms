import sys

def star(idx, jdx, num):
    if ((idx // num) % 3 == 1) & ((jdx // num) % 3 == 1):
        sys.stdout.write(' ')
    else:
        if (num // 3 == 0):
            sys.stdout.write('*')
        else:
            star(idx, jdx, num / 3)
    

num = int(input())

for idx in range(num):
    for jdx in range(num):
        star(idx, jdx, num)
    sys.stdout.write('\n')