import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        fre , n , ans , removed = Counter(arr) , len(arr)//2 , 0 ,0
        values =[-value for value in fre.values()]
        heapq.heapify(values) # the heappop need a heap to be functional
        while removed < n:
            removed += -(heapq.heappop(values))
            ans += 1
        return ans
