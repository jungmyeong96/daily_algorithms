import sys

mNum = sys.stdin.readline().split('-')

nums = []

for i in mNum:
    pNum = i.split('+')
    num = 0
    for j in pNum:
        num += int(j)
    nums.append(num)
n = nums[0]
for i in range(1, len(nums)):
    n -= nums[i]

sys.stdout.write(f'{n}\n')