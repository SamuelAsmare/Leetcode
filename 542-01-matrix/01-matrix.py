from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        ans = [[0]*m for _ in range(n)]
        visited = set()
        que = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    que.append((i,j))
                    visited.add((i,j))

        directions = [(0,1),(0,-1)
        ,(1,0),(-1,0)]
        while que:
            row, col = que.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < m and (nr,nc) not in visited:
                    ans[nr][nc] = ans[row][col] + 1
                    visited.add((nr,nc))
                    que.append((nr,nc))

        return ans


        