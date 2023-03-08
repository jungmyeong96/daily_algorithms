import collections

def removeDuplicateLetters(s: str) -> str:
    #1.stack연산을 통한 구현
    # counter, stack = collections.Counter(s), []

    # for char in s:
    #     counter[char] -= 1 #해당 문자 삽입을 시도할 때마다 하나씩 줄음
    #     if char in stack:
    #         continue
    #     #뒤에 붙일 문자가 남아 있다면 스택에서 제거
    #         #추가할 문자가 스택문자보다 사전적으로 앞에 있는지 순서 비교
    #         #스택문자가 counter에 남아 있는지 체크
    #     while stack and char < stack[-1] and counter[stack[-1]] > 0:
    #         stack.pop()
    #     stack.append(char)
    #     # print(char, stack, counter[char])
    # return ''.join(stack)

    #2. stack연산과 검사로직 분리
    counter, stack, seen = collections.Counter(s), [], set()

    for char in s:
        counter[char] -= 1 #해당 문자 삽입을 시도할 때마다 하나씩 줄음
        #원래 사실상 요소가 이미 처리되었는지 검사하는 기능은 stack에 없기에 set을 추가
        if char in seen:
            continue
        #뒤에 붙일 문자가 남아 있다면 스택에서 제거
            #추가할 문자가 스택문자보다 사전적으로 앞에 있는지 순서 비교
            #스택문자가 counter에 남아 있는지 체크
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
        # print(char, stack, counter[char])
    return ''.join(stack)

print(removeDuplicateLetters('cbacdcbc'))