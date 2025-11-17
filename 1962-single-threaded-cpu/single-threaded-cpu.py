class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i , item in enumerate(tasks):
            item.append(i)
        tasks.sort(key = lambda x : (x[0],x[1]))
        time = tasks[0][0]
        heap = []
        i = 0
        time = 0
        ans = []
        while i < len(tasks) or heap:
            if not heap:
                time = max(time, tasks[i][0])
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1
            procTime, idx = heapq.heappop(heap)
            time += procTime
            ans.append(idx)
        return ans
