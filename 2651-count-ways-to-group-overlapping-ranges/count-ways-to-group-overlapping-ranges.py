class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ranges.sort()
        container = ranges[0][1]
        containers_count = 1   # first container
        for start, end in ranges[1:]:
            if start > container:  # new non-overlapping block
                containers_count += 1
                container = end
            else: 
                container = max(container, end)
        ans = pow(2, containers_count, MOD)
        return ans

