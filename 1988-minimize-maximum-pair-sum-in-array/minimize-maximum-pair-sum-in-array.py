class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left , right , ans = 0 , len(nums)-1 , float("-inf")
        while left < right:
            ans = max(ans , nums[left] + nums[right])
            left += 1
            right -= 1
        return ans
