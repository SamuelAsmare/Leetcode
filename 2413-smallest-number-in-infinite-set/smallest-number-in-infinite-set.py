import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1 
        self.added_back = [] 
        self.in_heap = set() 
    def popSmallest(self):
        if self.added_back:
            smallest = heapq.heappop(self.added_back)
            self.in_heap.remove(smallest)
            return smallest
        else:
            val = self.curr
            self.curr += 1
            return val
    def addBack(self, num):
        if num < self.curr and num not in self.in_heap:
            heapq.heappush(self.added_back, num)
            self.in_heap.add(num)
