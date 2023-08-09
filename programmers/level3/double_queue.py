from collections import deque

def solution(operations):
    answer = []
    checker = deque()
    # answer = heapq(answer)
    
    for o in operations:
        command, value = o.split()
        if command == "I":
            checker.append(int(value))
            checker = deque(sorted(checker))
            # heappush(answer, int(value))
        elif command == "D" and value == "-1" and len(checker) > 0:
            # heappop(answer,)
            checker.popleft()
        elif command == "D" and value == "1" and len(checker) > 0:
            checker.pop()
    if len(checker) == 0:
        answer = [0, 0]
    else:
        answer.append(max(checker))
        answer.append(min(checker))
    return answer