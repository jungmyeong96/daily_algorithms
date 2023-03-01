from typing import List

def arrayPairSum(nums: List[int]) -> int:
    #1. 기본적인 정렬을 통한 방식
    # Runtime 281 ms
    # nums.sort()
    # sum = 0
    # for i in range(0, len(nums) - 1, 2):
    #     sum += nums[i]
    # return sum
    
    #2. 슬라이싱을 통한 방식
    #Runtime 269 ms
    return sum(sorted(nums)[::2])

print(arrayPairSum([1,4,3,2]))