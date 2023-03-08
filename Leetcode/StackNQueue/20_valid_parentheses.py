
def isValid(s: str) -> bool:
    #1. list를 사용하고 일일이 비교하는 코드
    # stack = list()

    # for i in range(len(s)):
    #     if s[i] == '(' or s[i] == '[' or s[i] == '{':
    #         stack.append(s[i])
    #     else:
    #         if len(stack) == 0:
    #             return False
    #         last = stack.pop()
    #         if (last == '(' and s[i] != ')') or \
    #             (last == '[' and s[i] != ']') or \
    #             (last == '{' and s[i] != '}'):
    #             return False
    # if len(stack) != 0:
    #     return False
    # return True
    #2. dict mapping으로 비교를 간소화
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    #스택 이용 예외 처리 및 일치여부 판별
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0