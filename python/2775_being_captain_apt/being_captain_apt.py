testcode = int(input())

for _ in range(testcode):
    floor = int(input())
    room = int(input())
    result = [x for x in range(1, room + 1)]
    print(result)   
    for _ in range(floor):
        for i in range(1, room):
            result[i] += result[i - 1]
    print(result)
