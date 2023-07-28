from typing import List

class Solution:
    # 재귀 분할정복
    # 연산자기준 분할
    # 종료조건 숫자만 있을 때 하나 숫자 리스트 반환
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left: List[int], right: List[int], op: str) -> List[int]:
            result = []
            for l in left:
                for r in right:
                    result.append(eval(str(l) + op + str(r)))
            return result



        if expression.isdigit():
            return[int(expression)]
        
        result = []

        for i, v in enumerate(expression):
            if v in "-+*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                result.extend(compute(left, right, v))
        return result


expression = "2*3-4*5"
print(Solution().diffWaysToCompute(expression))