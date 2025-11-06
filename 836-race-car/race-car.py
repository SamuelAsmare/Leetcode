class Solution:
    def racecar(self, target: int) -> int:
        # the car can reach to the target in diffferent ways by accelarating and reversing
        # so each individual destinations can give us nodes of a graph
        q = deque([(0,0,1)]) # steps  , position and speed
        visited = set([0,1])
        while q:
            steps , position , speed = q.popleft()
            if position == target :
                return steps
            if (position,speed) in visited:
                continue
            visited.add((position,speed))
            q.append((steps + 1, position + speed , speed*2))
            q.append((steps + 1, position ,-1 if speed > 0 else 1))
