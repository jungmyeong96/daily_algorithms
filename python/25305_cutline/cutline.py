
num_of_people, cutline = map(int,input().split())

score = list(map(int, input().split()))

score.sort(reverse=True)

print(score[cutline - 1])

