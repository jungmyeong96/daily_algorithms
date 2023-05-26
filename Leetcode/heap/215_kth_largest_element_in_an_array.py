class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1.직접 heap을 구성해서 만드는 구조
        # heap = list()
        # for n in nums:
        #     heapq.heappush(heap, -n)
        
        # for _ in range(1, k):
        #     heapq.heappop(heap)
        
        # return -heapq.heappop(heap)

        # 2.heapfy이용
        # heapq.heapify(nums)

        # for _ in range(len(nums) - k):
        #     heapq.heappop(nums)
        
        # return heapq.heappop(nums)

        # 3.heapq largest
        # return heapq.nlargest(k, nums)[-1]

        # 4. 입력값 고정시 정렬을 이용 성능이 가장 좋음
        return sorted(nums, reverse=True)[k - 1]
