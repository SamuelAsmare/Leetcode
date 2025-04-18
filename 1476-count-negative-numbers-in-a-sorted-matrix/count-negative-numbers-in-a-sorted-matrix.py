class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        tot=0
        for i in range(len (grid)):
            for j in range (len (grid[i])):
                if(grid[i][j] <0):
                    tot+=1
        return tot      # 1351
