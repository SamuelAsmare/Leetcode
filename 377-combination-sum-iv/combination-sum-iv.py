class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        memo[0] = 1
        def dfs(target):
            if target in memo or target < 0:
                return memo[target]
            for num in nums:
                memo[target] += dfs(target-num)
            return memo[target]
        return dfs(target)

                
        