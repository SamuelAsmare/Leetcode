class Solution:
    def climbStairs(self, n: int) -> int:
        dp = dict()
        def climb(n):
            if n==1 or n==0:
                return 1
            if n in dp:
                return dp[n]
            dp[n] = climb(n-1) + climb(n-2)
            return dp[n]
        return climb(n)
