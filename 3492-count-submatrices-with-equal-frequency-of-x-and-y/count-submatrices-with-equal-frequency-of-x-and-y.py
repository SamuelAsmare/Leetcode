class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n , m , ans = len(grid) , len(grid[0]) , 0
        for i in range(n):
            for j in range(m):
                nr , nc , x , y = i - 1 , j - 1 , 0 , 0
                if grid[i][j] == "X":
                    x = 1
                if grid[i][j] == "Y":
                    y = 1
                if 0 <= nr < n:
                    px  , py = grid[nr][j]
                    x += px 
                    y += py
                if 0 <= nc < m:
                    px  , py = grid[i][nc]
                    x += px 
                    y += py
                if 0 <= nr < n and 0 <= nc < m:
                    px , py = grid[nr][nc]
                    x -= px
                    y -= py
                if x == y and x:
                    ans += 1
                grid[i][j] = (x,y)
        return ans
                

 