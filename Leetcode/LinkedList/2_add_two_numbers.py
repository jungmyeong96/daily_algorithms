# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#1.ListNode를 역으로 변환 및 list화 시킨 후 연산하는 방법
#Runtime 67 ms
#Memory 14 MB

def reverseList(self, node: ListNode, prev: ListNode = None) -> ListNode:
    if not node:
        return prev
    next, node.next = node.next, prev
    return self.reverseList(next, node)
def toList(self, node: ListNode) -> ListNode:
    list: List = []
    while node:
        list.append(node.val)
        node = node.next
    return list
def toReverseListnode(self, num: str) -> ListNode:
    prev: ListNode = None
    for n in num:
        node = ListNode(n)
        node.next = prev
        prev = node
    return prev
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    rl1 = self.toList(self.reverseList(l1))
    rl2 = self.toList(self.reverseList(l2))

    # int배열 -> string으로 변환 -> int로 재변환 -> 연산
    # resultStr = int(''.join(map(str,rl1))) + int(''.join(map(str,rl2)))
    #reduce를 통해 가산 계산이 가능합니다. 
    #lambda 식에는 계산식, 대상 배열, 초기값이 설정되어 초기 x에는 0이 지정되어 시작됩니다.
    resultStr = functools.reduce(lambda x, y: 10 * x + y, rl1, 0) + functools.reduce(lambda x, y: 10 * x + y, rl2, 0)
    return self.toReverseListnode(str(resultStr))

#2.전가산기 구현 
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        #두 입력값의 합 계산
        #뒤집어져 있으니 순서대로 하나씩 더했을 때 나온 값을 10으로 나눈 몫만 잘 관리해주면 계산이된다.
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        #몫(자리올림수)과 나머지(값) 계산
        carry,val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next
    return root.next
        