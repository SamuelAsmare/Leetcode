class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n  = len(questions)
        dp = [0] * n
        def backtrack(i):
            if i >= n:
                return 0
            if dp[i]:
                return dp[i]
            points , brainpower = questions[i]
            dp[i] = max(backtrack(i + 1),
            points + backtrack(i + brainpower + 1))
            return dp[i]
        return backtrack(0)