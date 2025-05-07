class Solution(object):
    def sortColors(self, nums):
      
      track = True
      i=0
      while track:
        track = False
        for i in range(1, len(nums)):
            
            if nums[i]<nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
                track = True
    
    
