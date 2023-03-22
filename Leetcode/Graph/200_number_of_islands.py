from typing import List

class Solution:
    #1. dfs 백트래킹 기본 문제
    # def dfs(self, grid: List[List[str]], i: int, j: int):
    #     if i < 0 or i >= len(grid) or \
    #         j < 0 or j >= len(grid[0]) or \
    #             grid[i][j] != '1' :
    #             return
        
    #     grid[i][j] = '0'

    #     self.dfs(grid, i + 1, j)
    #     self.dfs(grid, i - 1, j)
    #     self.dfs(grid, i, j + 1)
    #     self.dfs(grid, i, j - 1)
        

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     if not grid:
    #         return 0
        
    #     count = 0
    #     for i in range(len(grid)):
    #         for j in range(len(grid[i])):
    #             if grid[i][j] == '1':
    #                 self.dfs(grid, i, j)
    #                 count += 1
    #     return count

    #2. 클래스 멤버 변수로 빼기
    # grid: List[List[str]]

    # def dfs(self, i: int, j: int):
    #     if i < 0 or i >= len(self.grid) or \
    #         j < 0 or j >= len(self.grid[0]) or \
    #             self.grid[i][j] != '1' :
    #             return
        
    #     self.grid[i][j] = '0'

    #     self.dfs(i + 1, j)
    #     self.dfs(i - 1, j)
    #     self.dfs(i, j + 1)
    #     self.dfs(i, j - 1)
        

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     self.grid = grid
        
    #     if not self.grid:
    #         return 0
        
    #     count = 0
    #     for i in range(len(self.grid)):
    #         for j in range(len(self.grid[i])):
    #             if self.grid[i][j] == '1':
    #                 self.dfs(i, j)
    #                 count += 1
    #     return count

    #3. Nested function 적용

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i: int, j: int):
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1' :
                    return
            
            grid[i][j] = '0'

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count

ans = Solution()

print(ans.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
