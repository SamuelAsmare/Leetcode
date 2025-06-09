class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return 0
            
            curr = grid[i][j]
            grid[i][j] = 0 
            max_gold = max(
                dfs(i+1, j),
                dfs(i-1, j),
                dfs(i, j+1),
                dfs(i, j-1)
            )
            
            grid[i][j] = curr  
            return curr + max_gold
        
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j))
        return ans
