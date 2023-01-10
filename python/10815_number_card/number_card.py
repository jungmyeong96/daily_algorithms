import sys

numOfCards = int(sys.stdin.readline())

cards = list(map(int,sys.stdin.readline().split()))

numOfCheckers = int(sys.stdin.readline())

checkers = list(map(int, sys.stdin.readline().split()))

cards.sort()

def binary_search(num):
    l = 0
    r = numOfCards - 1
    while l <= r :
        mid = (l + r) // 2
        if cards[mid] == num :
            return 1
        elif cards[mid] > num :
            r = mid - 1
        else:
            l = mid + 1
    return 0

for num in checkers:
    print(binary_search(num), end= ' ')
