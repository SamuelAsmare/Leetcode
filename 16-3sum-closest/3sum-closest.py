class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        distance = float("inf")
        for i in range(len(nums)-2):
            rem = target - nums[i]
            left , right = i + 1, len(nums) - 1
            while(left < right):
                if(nums[left] + nums[right] == rem):
                    if abs(nums[left] + nums[right] + nums[i] - target) < distance:
                        ans = nums[left] + nums[right] + nums[i]
                        distance = abs(nums[left] + nums[right] + nums[i] - target )
                    left += 1
                    right -= 1
                elif(nums[left] + nums[right] < rem):
                    if abs(nums[left] + nums[right] + nums[i] - target) < distance:
                        ans = nums[left] + nums[right] + nums[i]
                        distance = abs( nums[left] + nums[right] + nums[i] - target )
                    left += 1
                else:
                    if abs(nums[left] + nums[right] + nums[i] - target) < distance:
                        ans = nums[left] + nums[right] + nums[i]
                        distance = abs(nums[left] + nums[right] + nums[i] - target) 
                    right -= 1
        return ans


