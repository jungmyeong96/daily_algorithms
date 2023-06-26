from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 투포인터 사용
        # left, right = 0, len(numbers) - 1
        # while not left == right:
        #     if numbers[left] + numbers[right] < target:
        #         left += 1
        #     elif numbers[left] + numbers[right] > target:
        #         right -= 1
        #     else:
        #         return left + 1, right + 1 # 리턴값
    
        # 이진검색
        # for k, v in enumerate(numbers):
        #     left, right = k + 1, len(numbers) - 1
        #     expected = target - v #기준 K의 다음 인덱스부터 expected검색
        #     #이진검색으로 나머지 값 판별
        #     while left <= right:
        #         mid = left + (right - left) // 2
        #         if numbers[mid] < expected:
        #             left = mid + 1
        #         elif numbers[mid] > expected:
        #             right = mid - 1
        #         else:
        #             return k + 1, mid + 1

        # Bisect 모듈 + 슬라이싱
    #     for k, v in enumerate(numbers):
    #         expected = target - v
    #         i = bisect.bisect_left(numbers[k + 1:], expected)
    #         if i < len(numbers[k + 1:]) and numbers[i + k + 1] == expected:
    #             return k + 1, i + k + 2 

        # 슬라이싱 최소화 (속도개선)
        # for k, v in enumerate(numbers):
        #     expected = target - v
        #     nums = numbers[k + 1:]
        #     i = bisect.bisect_left(nums, expected)
        #     if i < len(nums) and numbers[i + k + 1] == expected:
        #         return k + 1, i + k + 2

        # 슬라이싱 제거 (속도개선)
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1) # bisect.bisect_left(a, x ,lo, hi)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1


print(Solution().twoSum([2,7,11,15], 9))