class Solution:
    def maxSubarraySum(self, nums, k):
        min_prefix = [float("inf")] * k
        min_prefix[k - 1] = 0  
        prefix = 0
        ans = float("-inf")
        for i, x in enumerate(nums):
            prefix += x
            r = i % k
            ans = max(ans, prefix - min_prefix[r])
            min_prefix[r] = min(min_prefix[r], prefix)
        return ans
