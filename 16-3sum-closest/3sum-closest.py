class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        for i in range(len(nums)-2):
            left , right = i + 1, len(nums) - 1
            while(left < right):
                s = nums[left] + nums[right] + nums[i]
                if s == target:
                    return s
                if abs(s - target) < abs(closest - target):
                    closest = s
                if (s < target):
                    left += 1
                else:
                    right -= 1
        return closest


