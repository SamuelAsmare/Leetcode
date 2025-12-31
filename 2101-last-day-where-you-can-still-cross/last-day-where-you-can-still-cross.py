class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def can_cross(day):
            grid = [[0]*col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1 

            visited = set()

            def dfs(r, c):
                if r == row - 1:
                    return True
                visited.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < row and
                        0 <= nc < col and
                        grid[nr][nc] == 0 and
                        (nr, nc) not in visited
                    ):
                        if dfs(nr, nc):
                            return True
                return False
            for j in range(col):
                if grid[0][j] == 0:
                    if dfs(0, j):
                        return True
            return False
        left, right = 0, len(cells)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if can_cross(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
