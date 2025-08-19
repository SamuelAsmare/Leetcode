class Solution(object):
    def sortColors(self, nums):
      flag = True
      i=0
      while flag:
        flag = False
        for i in range(1, len(nums)):
            
            if nums[i]<nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
                flag = True
    
    