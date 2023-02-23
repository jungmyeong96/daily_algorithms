from typing import List # list of str

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    ### 1번 풀이 ###
    # left = 0 # swiching 방식으로 해결하는 문제 메모리 재사용  in-place with O(1)제약해결
    # right = len(s) - 1
    # while left < right:
    #     s[left], s[right] = s[right], s[left]
    #     left += 1
    #     right -= 1

    ### 2번 풀이 ###
    # s[::-1] # 공간복잡도 에러

    ### 3번 풀이 ###
    #s[:] = s[::-1] # 공간복잡도제약을 해결하기 위해 원래 메모리 재사용  in-place with O(1)제약해결

    ### 4번 풀이 ###
    s.reverse() # 스트링이 아닌 리스트인 경우 기본적으로 제공되는 reverse함수도 하나의 방법이다
    print(s)

strList = ["a", "b", "c"]
reverseString(strList)