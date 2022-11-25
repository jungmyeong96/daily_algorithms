result = list(map(int, input().split()))
solution = [1, 1, 2, 2, 2, 8]
for i, (res, sol) in enumerate(zip(result, solution)):
    if (i != 5):
        print(sol - res, end=" ")
    else:
        print(sol - res)