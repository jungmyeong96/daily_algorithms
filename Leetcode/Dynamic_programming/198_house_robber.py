class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # for i in range(len(nums)):
        #     if i < 2:
        #         continue
        #     elif i == 2:
        #         nums[i] = nums[i] + nums[i - 2]
        #     else:
        #         nums[i] = max(nums[i] + nums[i - 2], nums[i] + nums[i - 3])
        # return max(nums)

        if len(nums) <= 2:
            return max(nums)
        
        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp.popitem()[1]