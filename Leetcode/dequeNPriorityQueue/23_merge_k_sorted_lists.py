# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        #각 연결 리스트의 루트를 힙에 저장
        #heapq는 최소 값을 부모로 저장합니다.
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
 
        #heap에 쌓인 데이터 추출
        while heap:
            #최소 노드 추출
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]
            
            #힙 추출 이후 다음 노드는 다시 저장
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
        return root.next