# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

    if head is None or left == right:
        return head
    
    root = start = ListNode(None)
    root.next = head

    #뒤집을 위치 선정
    for _ in range(left - 1):
        start = start.next
    end = start.next

    #반복하면서 주어진 범위와 횟수 만큼 노드를 차례대로 뒤집습니다.
    #start, tmp|end
    for _ in range(right - left):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    return root.next