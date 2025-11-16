class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre  = Counter(nums)
        heap = []
        for num , f in fre.items():
            heapq.heappush(heap,(f,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for f,num in heap]
