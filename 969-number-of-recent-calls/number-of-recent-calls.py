from collections import deque
class RecentCounter:
    def __init__(self):
        self.que = deque()
    def ping(self, t: int) -> int:
        self.que.append(t)
        while self.que and self.que[0] < t-3000:
            self.que.popleft()
        return len(self.que)