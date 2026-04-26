class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n , m = len(grid) , len(grid[0])
        visited = set()
        def dfs(par , curr):
            r , c  = curr
            if (r , c) in visited:
                return True
            visited.add((r , c))
            directions = [(-1 , 0) , (1 , 0) , (0 , -1) , (0 , 1)]
            for dr , dc in directions:
                nr , nc = r + dr , c + dc
                if (0 <= nr < n and 0 <= nc < m and
                    (nr , nc) and (nr , nc) != par) and grid[nr][nc] == grid[r][c]:
                    # executions
                    if dfs(curr , (nr , nc)):
                        return True
            return False
        for i in range(n):
            for j in range(m):
                if (i , j) not in visited:
                    if dfs((-1 , -1) ,(i , j)):
                        return True
        return False

                    

                    




