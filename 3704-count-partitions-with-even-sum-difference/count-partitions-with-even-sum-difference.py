class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans , total = 0 , sum(nums)
        for i in range(len(nums)-1):
            if not (nums[i] - total - nums[i])&1:
                ans += 1
            nums[i] += nums[i-1]
        return ans