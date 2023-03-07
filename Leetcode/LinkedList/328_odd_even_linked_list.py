# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #리스트를 홀과 짝으로 나눠  N/2 번의 반복을 통해 구하고, 홀수의 끝과 짝수의 시작을 연결
    if head is None:
        return None
    
    odd = head
    even = head.next
    even_head = head.next

    #반복하면서 홀짝 노드처리
    #even기준 값이 None이어야 odd의 마지막 값 구할 수 있다.
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next
    
    odd.next = even_head
    return head
