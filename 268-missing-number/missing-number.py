class Solution(object):
    def missingNumber(self, nums):
        init = nums[0]
        nums.extend([i for i in range(len(nums)+1)])
        for i in range(1,len(nums)):
            init = init^nums[i]
        print(nums)
        return init
        