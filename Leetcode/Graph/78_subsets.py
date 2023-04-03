from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    def dfs(index):
        result.append(sets[:])
        
        for i in range(index, len(nums)):
            sets.append(nums[i])
            dfs(i + 1)
            sets.pop()
        return
    result = []
    sets = []
    dfs(0)
    return result

print(subsets([1, 2, 3]))