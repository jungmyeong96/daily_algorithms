import collections 
import re

# def isPalindrome(s: str) -> bool: #64ms 
#     ans: Deque = collections.deque() ##코테 때 까먹지 않게 from없이 씀 
#     for char in s:
#         if char.isalnum():
#             ans.append(char.lower())
#     while len(ans) > 1:
#         if ans.popleft() != ans.pop():
#             return False
#     return True

def isPalindrome(s: str) -> bool: ## 정규식을 활용한 버전 36ms
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]

print(isPalindrome("aaa"))