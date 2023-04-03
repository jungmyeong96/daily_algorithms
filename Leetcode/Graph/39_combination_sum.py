def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #일반적인 중복조합버전 자신에서 하위만 나옴
    def dfs(index: int):
        check = sum(makeTarget)
        if check == target:
            result.append(makeTarget[:])
            return
        if check > target:
            return
        for i in range(index, len(candidates)):
            makeTarget.append(candidates[i])
            dfs(i)
            makeTarget.pop()
    
    result = []
    makeTarget = []

    dfs(0)

    return result

    # 중복조합 간단한버전
    # def dfs(csum, index, path):
    #     if csum < 0:
    #         return
    #     if csum == 0:
    #         result.append(path)
    #         return
    #     for i in range(index, len(candidates)):
    #         dfs(csum - candidates[i], i, path + [candidates[i]])
    # dfs(target, 0, [])
    # return result
    