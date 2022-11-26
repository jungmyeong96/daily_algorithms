
currtime = list(map(int,input().split()))

time = int(input())

hour = time // 60 

min = time % 60

currtime[0] = currtime[0] + (currtime[1] + min) // 60
currtime[1] = (currtime[1] + min) % 60

currtime[0] = (currtime[0] + hour) % 24

result = str(currtime[0]) + " " + str(currtime[1])
print(result)