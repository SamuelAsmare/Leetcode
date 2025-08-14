class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        center = len(nums)//2
        mean = nums[center]
        ans = 0
        for item in nums:
            ans += abs(item-mean)
        return ans