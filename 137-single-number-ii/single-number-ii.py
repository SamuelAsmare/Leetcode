class Solution(object):
    def singleNumber(self, nums):
       fre = Counter(nums)
       for i in range(len(nums)):
        if(fre[nums[i]]==1):
            return nums[i]
       
         

        