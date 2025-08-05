class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            row , col = len(grid) , len (grid[0])
            if i >= row or i < 0 or j >= col or j < 0 or grid[i][j] == "0":
                return 
            grid[i][j] = "0"
            dfs( i+1 , j) , dfs(i-1,j) , dfs(i,j-1) , dfs(i,j+1)
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    result += 1
        return result

              