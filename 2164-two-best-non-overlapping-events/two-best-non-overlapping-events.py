class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort( key = lambda x : (x[0] , x[1] )) # sort by starting time
        starts = [item[0] for item in events]
        max_values = [item[2] for item in events]
        n = len(events)
        maxval = float("-inf")
        for i in range(n-1,-1,-1):
            val = events[i][2]
            maxval = max(maxval , val)
            max_values[i] = maxval
        ans = max_values[0]
        for i in range(n):
            start , end , val = events[i]
            pos = bisect_right(starts , end)
            if pos < n:
                ans = max(ans , val + max_values[pos])
        return ans 
                

            
