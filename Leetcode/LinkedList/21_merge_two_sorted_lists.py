from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    
    
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # 1.일반 연결리스트로 푸는 방식

    # ans = None
    # if not list1 and not list2:
    #     return ans
    # elif not list1:
    #     return list2
    # elif not list2:
    #     return list1

    # if list1.val < list2.val:
    #     ans = list1
    #     list1 = list1.next
    # else:
    #     ans = list2
    #     list2 = list2.next  

    # ansIter = ans
    # while list1 or list2:
    #     if list1 == None:
    #         ansIter.next = list2
    #         break
    #     if list2 == None:
    #         ansIter.next = list1
    #         break
    #     if list1.val < list2.val:
    #         ansIter.next = list1
    #         ansIter = ansIter.next
    #         list1 = list1.next
    #     else:
    #         ansIter.next = list2
    #         ansIter = ansIter.next
    #         list2 = list2.next

    # return ans

    #2. 재귀적으로 푸는 방식 병합 정렬의 마지막조합과 비슷
    # l1과 l2를 비교 후 항상 적은 값이 l1에 올 수 있도록 스왑
    # 적은 값 리스트인 l1가 None이 되면 나머지를 l1으로 취급
    if (not list1) or (list2 and list1.val > list2.val):
        list1, list2 = list2, list1
    if list1:
        list1.next = self.mergeTwoLists(list1.next, list2)
    return list1

# print(mergeTwoLists([1,2,4], [1,3,4]))