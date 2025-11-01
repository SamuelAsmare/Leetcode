class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        # we have n number of containers with overlapping(possibly) ranges
        ranges.sort()
        container , ans = ranges[0][1] , 2
        for start , end in ranges[1:]:
            if start <= container:
                container = max(end , container)
            else:
                container = end
                ans = (ans*2)%(10**9 + 7)
        return ans

