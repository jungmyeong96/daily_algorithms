from collections import deque
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #1. deque로 변환해서 작업한 코드

    # deq: deque = deque()

    # #head값이 없으면 True
    # if not head:
    #     return True
    
    # node = head
    # while node is not None:
    #     deq.append(node.val)
    #     node = node.next
    
    # while len(deq) > 1:
    #     if deq.popleft() != deq.pop():
    #         return False
    # return True

    #2. runner를 이용한 연결리스트 풀이법
    #역순으로 정렬할 rev head
    rev = None
    slow = fast = head

    #런너를 이용해 역순 연결리스트를 구성
    #fast는 두칸씩 건너뛰어 slow를 중간에 오는 시점으로 배치
    while fast and fast.next:
        fast = fast.next.next
        #다중할당을 사용하여 동일참조 방지
        # rev = 1->2, rev.next = None, rev = 1 -> None, slow = 2->2
        rev, rev.next, slow = slow, rev, slow.next
    
    # 연결리스트가 홀수이면 중간 값을 지나가야한다.
    if fast:
        slow = slow.next
    
    #펠린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev
    