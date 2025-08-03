class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for left in range(len(nums)-3,-1,-1):
            mid , right = left + 1 , left + 2
            if nums[right] < nums[mid] + nums[left]:
                return nums[right] + nums[mid] + nums[left]             
        return 0