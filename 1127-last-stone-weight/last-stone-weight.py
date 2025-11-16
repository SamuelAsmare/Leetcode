class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for weight in stones: # our max heap is built
            heappush(max_heap,-weight)
        while len(max_heap) >= 2:
            x = -(heapq.heappop(max_heap))
            y = -(heapq.heappop(max_heap))
            if x != y:
                y  = max(x,y) - min(x,y)
                heapq.heappush(max_heap,-(y))
        return -max_heap[0] if len(max_heap) == 1 else 0

