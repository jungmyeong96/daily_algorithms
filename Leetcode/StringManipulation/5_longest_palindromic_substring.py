## DP로 풀기도 하지만 느리다

def longestPalindrome(s: str) -> str:
    if len(s) < 2 or s == s[::-1]: # 파이썬의 문자열 슬라이싱은 매우 빠르기 때문에 조건을 걸면 속도향상에 도움이 된다.
        return s
    
    # 양옆으로 포인터를 확장하여 펠린드롬 검색
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    result = ''

    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    
    return result

print(longestPalindrome('babda'))