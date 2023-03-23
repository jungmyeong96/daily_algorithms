class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            # 전달받은 digits 인덱스에 따라 위치 변경
            for i in range(index, len(digits)):
                # 해당 digit의 소속 값 나열
                for j in pad[digits[i]]:
                    dfs(i + 1, path + j)

        if not digits:
            return []

        pad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
         "7": "pqrs", "8": "tuv", "9": "wxyz"}

        result = []
        dfs(0, "")
        return result