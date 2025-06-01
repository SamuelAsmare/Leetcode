class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        row , cols = len(grid)-1,len(grid[0]) -1
        for i in range(row+1):
            for j in range(cols+1):
                if i+1 <= row: 
                    if grid[i+1][j] != grid[i][j]:
                        return False
                if j+1 <= cols:
                    if grid[i][j]==grid[i][j+1]:
                        return False
        return True