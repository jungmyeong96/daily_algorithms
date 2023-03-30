import itertools
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    #1. DFS를 활용한 방법
    # result = []
    # elements_set = []

    # def dfs(elements):
    #     if len(elements) == 0:
    #         result.append(elements_set[:])
    #         return
    #     for i in elements:
    #         check_nums = elements[:]
    #         check_nums.remove(i)
            
    #         elements_set.append(i)
    #         dfs(check_nums)
    #         elements_set.pop()
    #     return
    
    # dfs(nums)
    # return result
    
    #2. itertools를 활용하는 법
    return list(map(list, itertools.permutations(nums)))

print(permute([1, 2, 3]))