class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = first_min = second_min = nums[0] 
        nums[1:] = sorted(nums[1:])
        ans += nums[1] + nums[2]
        return ans 
        