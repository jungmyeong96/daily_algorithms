from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #1. 브루트 포스
        # result: Set = set()
        # for n1 in nums1:
        #     for n2 in nums2:
        #         if n1 == n2:
        #             result.add(n1)
        # return result

        #2.이진 검색
        # result: Set = set()
        # # 이진검색을 위한 배열정렬
        # nums2.sort()
        # for n1 in nums1:
        #     #이진 검색으로 일치여부 판별
        #     i2 = bisect.bisect_left(nums2, n1)
        #     if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
        #         result.add(n1)
        # return result

        #3. 투포인터
        result: Set = set()
        # 양쪽 모두 정렬
        nums1.sort()
        nums2.sort()
        i = j = 0
        #투 포인터 우측으로 이동하며 일치 여부 판별
        while i < len(nums1) and  j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result. add(nums1[i])
                i += 1
                j += 1
        return result 

print(Solution().intersection([1,3,5,4,0], [2,1]))