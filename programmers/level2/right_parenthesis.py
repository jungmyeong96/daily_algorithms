from collections import deque

def solution(s):
    answer = True
    
    s_stack = deque()
    
    for c in s:
        if c == '(':
            s_stack.append('(')
        elif c == ')' and len(s_stack) == 0:
            answer = False
        elif c == ')' and s_stack[-1] == '(':
            s_stack.pop()

    if len(s_stack) != 0:
        answer = False
    return answerx