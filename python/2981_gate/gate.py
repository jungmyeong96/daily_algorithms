N = int(input())

# nums = []

# for idx in range(N):
#     nums.append(int(input()))

# nums.sort()

#minNum = min(nums)

# for idx in range(2, nums[0] + 1):
#     checker = -1
#     for jdx in range(1, N):
#         if checker == -1:
#             checker = nums[jdx] % idx
#         if checker != nums[jdx] % idx:
#             break
#         if jdx == N - 1:
#             print(idx, end=" ")
    

nums = list(int(input()) for _ in range(N))
nums.sort()
interval = []
ans = []

def findGCD(a, b):
    if b == 0:
        return a
    else:
        return findGCD(b, a % b)

#A = M * a + R
#B = M * b + R

# A - B = M(a - b)
#찾고자하는 M은 A - B의 약수
for i in range(1, N):
    interval.append(nums[i] - nums[i - 1])

prev = interval[0] #가장 작은 수 부터 최대공약수 탐색
for i in range(1, len(interval)):
    prev = findGCD(prev, interval[i])

for i in range(2, int(prev ** 0.5) + 1): #최대공약수의 약수를 뽑아냄
    if prev % i == 0:
        ans.append(i)
        ans.append(prev//i)
ans.append(prev) #제곱근 추가
ans = list(set(ans))
ans.sort()
print(*ans)
