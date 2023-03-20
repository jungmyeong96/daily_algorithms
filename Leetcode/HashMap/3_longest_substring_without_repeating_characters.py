def lengthOfLongestSubstring(s: str) -> int:
    checked = {}
    max_len = start = 0

    for index, char in enumerate(s):
        #substring에 속하는 이미 등장한 문자의 경우 start 위치를 해당인덱스 앞으로 변경
        if char in checked and start <= checked[char]:
            start = checked[char] + 1
        else:
            max_len = max(max_len, index - start + 1)
        
        #현재 문자를 키로한 인덱스 삽입
        checked[char] = index
    return max_len

print(lengthOfLongestSubstring("abcabccc"))