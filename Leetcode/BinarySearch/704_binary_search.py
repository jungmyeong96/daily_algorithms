class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #재귀적 해결
        # def binary_search(left, right):
        #     if left <= right:
        #         mid = (left + right) // 2

        #         if nums[mid] < target:
        #             return binary_search(mid + 1, right)
        #         elif nums[mid] > target:
        #             return binary_search(left, mid - 1)
        #         else:
        #             return mid
        #     else:
        #         return - 1
        # return binary_search(0, len(nums) - 1)

        # # 재귀 제한으로 인한 반복으로 변경
        # left = 0
        # right = len(nums) - 1

        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] < target:
        #         left = mid + 1
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         return mid
        # return -1

        # 이진 검색 모듈
        # index = bisect.bisect_left(nums, target)

        # if index < len(nums) and nums[index] == target:
        #     return index
        # return -1

        #파이썬 제공 모듈로 처리
        try:
            return nums.index(target)
        except ValueError:
            return -1