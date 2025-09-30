import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top = nums
        heapq.heapify(self.top)
        while len(self.top) > k:
            heapq.heappop(self.top)

    def add(self, v: int) -> int:
        heapq.heappush(self.top, v)
        if len(self.top) > self.k:
            heapq.heappop(self.top)
        return self.top[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)