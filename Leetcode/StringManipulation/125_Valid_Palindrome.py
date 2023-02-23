import collections 

def isPalindrome(s: str) -> bool:
    ans: Deque = collections.deque() ##코테 때 까먹지 않게 from없이 씀
    for char in s:
        if char.isalnum():
            ans.append(char.lower())
    while len(ans) > 1:
        if ans.popleft() != ans.pop():
            return False
    return True

print(isPalindrome("aaa"))