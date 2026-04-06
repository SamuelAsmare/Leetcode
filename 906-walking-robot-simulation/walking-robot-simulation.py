class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        root = (0 , 0)
        walls = set()
        for u,v in obstacles:
            walls.add((u ,v))    
        directions = [[0 , 1] , [1, 0 ]  , [ 0 , -1] , [ -1 , 0]]
        Dir = 0 
        ans = 0
        for index , item in enumerate(commands):
            if item == -1:
               Dir = (Dir + 1)%4
            elif item == -2:
                Dir = (Dir - 1)%4
            else:
                x , y = directions[Dir]
                for _ in range(item):
                    u , v = root
                    if (u + x , v+y) in walls:
                        break
                    ans = max((u + x)**2 + (y + v)**2 , ans)
                    root = (u + x , v + y)
        return ans
# root = [1 , 4] Dir = 0 , [6,-1,-1,6] 

