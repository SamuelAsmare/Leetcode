from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        que = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    que.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        minutes = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while que and fresh > 0:
            for _ in range(len(que)):
                x, y = que.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        que.append((nx, ny))
            minutes += 1
        return minutes if fresh == 0 else -1
