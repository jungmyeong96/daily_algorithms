# import sys

# N = int(sys.stdin.readline())

# numbers = list(map(int, sys.stdin.readline().split()))

# plus, minus, multi, divide = map(int, sys.stdin.readline().split())

# operators = []

# checkUsage = [False for _ in range(N - 1)]

# selectedOperators = []

# results = []

# def add_operator(tag, count):
#     for _ in range(count):
#         operators.append(tag)

# add_operator('+', plus)
# add_operator('-', minus)
# add_operator('*', multi)
# add_operator('/', divide)

# def calc_num():
#     num = numbers[0]
#     for idx in range(N - 1):
#         if selectedOperators[idx] == '+':
#             num += numbers[idx + 1]
#         elif selectedOperators[idx] == '-':
#             num -= numbers[idx + 1]
#         elif selectedOperators[idx] == '*':
#             num *= numbers[idx + 1]
#         elif selectedOperators[idx] == '/':
#             if num < 0 and numbers[idx + 1] > 0:
#                 num = ((num * -1) // numbers[idx + 1]) * -1
#             else: 
#                 num = num // numbers[idx + 1]
#     return num

# def dfs(x):
#     if x == N - 1:
#         results.append(calc_num())
#         return
#     for idx in range(N - 1):
#         if checkUsage[idx]:
#             continue 
#         checkUsage[idx] = True
#         selectedOperators.append(operators[idx])
#         dfs(x + 1)
#         checkUsage[idx] = False
#         selectedOperators.pop()


# dfs(0)

# sys.stdout.write("%d\n" % max(results))
# sys.stdout.write("%d\n" % min(results))



import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

plus, minus, multi, divide = map(int, sys.stdin.readline().split())

operators = []

checkUsage = [False for _ in range(N - 1)]

results = []

def add_operator(tag, count):
    for _ in range(count):
        operators.append(tag)

add_operator('+', plus)
add_operator('-', minus)
add_operator('*', multi)
add_operator('/', divide)

def calc_num(op, value, num):
    if op == '+':
        value += num
    elif op == '-':
        value -= num
    elif op == '*':
        value *= num
    elif op == '/':
        if value < 0 and num > 0:
            value = ((value * -1) // num) * -1
        else: 
            value = value // num
    return value

def dfs(x, value):
    if x == N - 1:
        results.append(value)
        return
    for idx in range(N - 1):
        if checkUsage[idx]:
            continue 
        checkUsage[idx] = True
        sum = calc_num(operators[idx], value, numbers[x + 1])
        dfs(x + 1, sum)
        checkUsage[idx] = False


dfs(0, numbers[0])

sys.stdout.write("%d\n" % max(results))
sys.stdout.write("%d\n" % min(results))



# # 연산자 끼워 넣기

# n = int(input())
# data = list(map(int,input().split()))
# cal = list(map(int,input().split()))

# max_number = -1e9
# min_number = 1e9

# def dfs(depth, value, p, m, mu, d):

#     global max_number, min_number

#     if depth == n:
#         max_number = max(value, max_number)
#         min_number = min(value, min_number)
#         return
    
#     if p > 0:
#         dfs(depth + 1, value + data[depth], p - 1, m, mu, d)
#     if m > 0:
#         dfs(depth + 1, value - data[depth], p, m - 1, mu, d)
#     if mu > 0:
#         dfs(depth + 1, value * data[depth], p, m, mu - 1, d)
#     if d > 0:
#         dfs(depth + 1, int(value / data[depth]), p, m, mu, d - 1)

# dfs(1, data[0], cal[0], cal[1], cal[2], cal[3])

# print(max_number)
# print(min_number)