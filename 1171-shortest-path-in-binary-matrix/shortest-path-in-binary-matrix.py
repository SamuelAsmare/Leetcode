from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # que , visit ,
        r , c = len(grid) , len(grid[0])
        que = deque([(0,0,1)])
        visit = set((0,0))
        # left , right , up , down , upleft , upright , downleft , downright
        directions = [[0,-1] , [0,1] , [-1 , 0] , [1,0] , [-1,1] , [-1,-1] , [1,-1] , [1,1]]
        while que:
            row , col , length  = que.popleft()
            if row < 0 or row >=  r or col < 0 or col >= c or grid[row][col]==1 :
                continue
            elif row == r-1 and col == c-1:
                return length
            else:
                for dirr , dirc in directions:
                    if (row+dirr , col+dirc) not in visit:
                        que.append((row+dirr , col+dirc , length+1))
                        visit.add((row+dirr , col+dirc))
        return -1

