from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        y, x = entrance
        q = deque([(y, x, 0)])
        maze[y][x] = "+" 
        while q:
            r, c, dist = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and maze[nr][nc] == ".":
                    if nr == 0 or nc == 0 or nr == row-1 or nc == col-1:
                        return dist + 1
                    maze[nr][nc] = "+"  
                    q.append((nr, nc, dist + 1))

        return -1
