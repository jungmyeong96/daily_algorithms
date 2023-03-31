
def combine(self, n: int, k: int) -> List[List[int]]:
    #1.dfs를 이용한 해결
    # result = []
    # check_nums = []
    # def dfs(start: int, k: int):
    #     if k == 0:
    #         result.append(check_nums[:])
        
    #     for i in range(start, n + 1):
    #         check_nums.append(i)
    #         dfs(i + 1, k - 1)
    #         check_nums.pop()

        
    # dfs(1, k)
    # return result
    #2. itertools
    return list(itertools.combinations(range(1, n + 1), k))