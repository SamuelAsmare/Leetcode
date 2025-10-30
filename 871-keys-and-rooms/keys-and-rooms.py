from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n  , visited = len(rooms) , set([0])
        que = deque([0])
        while que:
            r = que.popleft()
            for key in rooms[r]:
                if key not in visited:
                    visited.add(key)
                    que.append(key)
                else:
                    continue
        return len(visited)==n

            


