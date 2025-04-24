class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n=len(grid)-1
        for i in range(len (grid)):
            for j in range(len(grid)):
                if (i==j):
                    if (grid[i][j]==0):
                        return False
                    else:
                        continue
                elif(j == n-i):
                    if (grid[i][j]==0):
                        return False
                elif( i != j):
                    if (grid[i][j]!= 0 ):
                        return False
        return True