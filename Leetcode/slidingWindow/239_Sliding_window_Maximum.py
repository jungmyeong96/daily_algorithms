from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue
        
            #새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v
            
            result.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')

        return result
    
print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
