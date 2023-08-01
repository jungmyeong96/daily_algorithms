from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sums: List[int] = [nums[0]]
        # for i in range(1, len(nums)):
        #     sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))
        # return max(sums)
        
        # 공간복잡도 절약
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0)
        # return max(nums)

        # 카제인 알고리즘
        best_sum = -sys.maxsize
        curr_sum = 0
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            best_sum = max(best_sum, curr_sum)
        return best_sum


nums= [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#nums = [-1, -2]
print(Solution().maxSubArray(nums))