class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        n = len(triangle)
        memo = triangle[-1]
        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                memo[j] = triangle[i][j] + min(memo[j], memo[j+1])
        return memo[0]