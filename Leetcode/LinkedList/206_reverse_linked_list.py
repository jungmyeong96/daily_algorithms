# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #1. 재귀적 백트래킹을 해결
    #Runtime 42 ms
    #Memory 20.4 MB
    #node는 진행방향, prev는 reverse값 저장
    # def reverse(node: ListNode, prev: ListNode = None):
    #     if not node:
    #         return prev
    #     next, node.next = node.next, prev
    #     return reverse(next, node)
    # return reverse(head)

    #2. 반복으로 해결
    #Runtime 15ms
    #Memory 15.5 MB
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    
    return prev
