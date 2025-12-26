class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top_prefix = grid[0][:]
        for i in range(n-2, -1, -1):
            top_prefix[i] += top_prefix[i+1]
        
        bottom_prefix = grid[1][:]
        for i in range(1, n):
            bottom_prefix[i] += bottom_prefix[i-1]
        
        ans = float('inf')
        for i in range(n):
            top_remaining = top_prefix[i+1] if i+1 < n else 0
            bottom_remaining = bottom_prefix[i-1] if i-1 >= 0 else 0
            ans = min(ans, max(top_remaining, bottom_remaining))
        return ans
