class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n , m , ans = len(grid) , len(grid[0]) , 0
        for i in range(n):
            for j in range(m):
                nr , nc = i - 1 , j - 1
                if 0 <= nr < n:
                    grid[i][j] += grid[nr][j]
                if 0 <= nc < m:
                    grid[i][j] += grid[i][nc]
                if 0 <= i-1 <= n and 0 <= j-1 <= m:
                    grid[i][j] -= grid[i-1][j-1]
                if grid[i][j]  <= k:
                    ans += 1
        return ans
