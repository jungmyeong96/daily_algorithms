import sys

numOfCards = int(sys.stdin.readline())

cards = sorted(list(map(int, sys.stdin.readline().split())))

numOfCheckers = int(sys.stdin.readline())

checkers = list(map(int, sys.stdin.readline().split()))

dict_checker = {}

for i in cards:
    if i in dict_checker: 
        dict_checker[i] += 1
    else:
        dict_checker[i] = 1        

for i in checkers:
    if i in dict_checker:
        sys.stdout.write("%s " % dict_checker[i])
    else:
        sys.stdout.write("0 ")
