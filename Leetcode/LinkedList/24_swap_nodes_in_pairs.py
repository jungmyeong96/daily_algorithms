# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #1. 반복 구조로 스왑
    # root = prev = ListNode(None)
    # prev.next = head

    # while head and head.next:
    #     # b가 a(head)를 가리키도록 할당 (교환)
    #     b = head.next
    #     head.next = b.next 
    #     b.next = head

    #     #prev가 b를 가리키도록 할당 (페어를 연결)
    #     prev.next = b

    #     #다음번 비교를 위해 이동 (이동)
    #     head = head.next
    #     prev = prev.next.next

    # return root.next

    #2. 재귀 구조로 스왑
    if head and head.next:
        p = head.next
        #스왑된 값 리턴 받음
        head.next = self.swapPairs(p.next)
        p.next = head
        return p
    return head
