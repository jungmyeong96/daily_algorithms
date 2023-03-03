
from typing import List


# 브루트포스
# Runtime 3639 ms
def twoSum(nums: List[int], target: int) -> List[int]: 
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# for반복문 대신 in 연산을 사용 똑같이 O(n^2)이지만 훨씬 가볍다  
# Runtime 623 ms
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     for i, n in enumerate(nums):
#         complement = target - n
    
#         if complement in nums[i + 1:]:
#             return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

#dictionary 같은 경우는 조회가 평균적으로 O(1)에 가능하기 때문에 시간복잡도를 O(N)으로 줄일 수 있습니다.
#Runtime 56 ms
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i
    
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]
            
print(twoSum([2,7,11,15], 9))