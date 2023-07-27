class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #부르트 포스
        # for n in nums:
        #     if nums.count(n) > len(nums) // 2 :
        #         return n

        #DP
        # counts = collections.defaultdict(int)
        # for n in nums:
        #     if counts[n] == 0:
        #         counts[n] = nums.count(n)
        #         if counts[n] > len(nums) // 2:
        #             return n

        #분할정복
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > len(nums) // 2]

        # 파이썬
        #return sorted(nums)[len(nums) // 2]
