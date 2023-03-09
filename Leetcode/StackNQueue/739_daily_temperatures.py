def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #순서대로 처리할 수 없고, 인덱스에 따른 처리를 할 것이기 때문에 배열을 미리 생성
    answer = [0] * len(temperatures)
    stack = []
    for i, cur in enumerate(temperatures):
        #현재 온도가 스택 값보다 높다면 처리 후 저장
        #[73] -> [74] -> [75, 71, 69] -> [75] -> [76, 73]
        while stack and cur > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer