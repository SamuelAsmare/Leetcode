class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n , m = len(grid) , len(grid[0])
        rows , row_sum = [0] * n , 0
        columns , column_sum = [0] * m , 0
        for i in range(n):
            for j in range(m):
                rows[i] += grid[i][j]
                columns[j] += grid[i][j]
                row_sum += grid[i][j]
                column_sum += grid[i][j]
        prefix = 0
        for i in range(n-1):
            prefix += rows[i]
            row_sum -= rows[i]
            if prefix == row_sum:
                return True
        prefix = 0
        for i in range(m-1):
            prefix += columns[i]
            column_sum -= columns[i]
            if prefix == column_sum:
                return True
        return False



    


        
        