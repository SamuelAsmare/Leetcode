class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # we are using BFS , left , right , up down
        row , col = len(maze) , len(maze[0])
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        standy , standx = entrance
        q = deque([(standy , standx , 0)])
        visited = set([(standy,standx)])
        while q:
            r , c , distance = q.popleft()
            for nr , nc in directions:
                if not (0 <= nr  + r < row and 0 <= nc + c < col):
                    if distance != 0:
                        print((r,c))
                        return distance
                else:
                    if maze[nr+r][nc+c] == "." and (nr+r ,nc+c) not in visited:
                        q.append((nr+r,nc+c , distance+1))
                        visited.add((nr+r,nc+c))
        return -1
            
