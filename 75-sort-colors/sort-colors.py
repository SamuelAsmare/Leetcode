class Solution(object):
    def sortColors(self, nums):
      for i in range(0,len(nums),+1):
        for j in range(len(nums)-1,i,-1):
            if(nums[i]>nums[j]):
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp