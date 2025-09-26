class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        ans = 0
        for right in range(len(nums)- 1, 1, -1):  
            middle = right - 1
            left = 0
            while left < middle:
                if nums[left ] + nums[middle] > nums[right]:
                    ans += middle - left    
                    middle -= 1
                else:
                    left += 1
        return ans
