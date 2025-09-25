class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        colmax , rowmax , n  = [] , [] , len(grid)
        for item in grid : 
            rowmax.append(max(item))
        for i in range(n):
            val = 0 
            for j in range(n):
                val = max(val , grid[j][i])
            colmax.append(val)
        total = 0
        for row in range (n) : 
            for col in range(n) :
                minval = min(colmax[col] , rowmax[row])
                total += (minval - grid[row][col] )
        return total


