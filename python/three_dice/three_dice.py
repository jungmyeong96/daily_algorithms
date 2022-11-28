
dices = list(map(int, input().split()))

counter = {}
result = 0

for value in dices:
    try: counter[value] += 1
    except: counter[value] = 1

for key, value in counter.items():
    if (value == 3):
        result = 10000 + key * 1000
    elif (value == 2):
        result = 1000 + key * 100
if result == 0:
    result = max(dices) * 100
print(result)

# if (len(set(dices)) == 1)
#     return 10000 + dices[0] * 1000
# else if (len(set(dices)) == 2)
# {
    
# }
# else
