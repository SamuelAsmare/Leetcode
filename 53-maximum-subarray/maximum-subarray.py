class Solution:
    def maxSubArray(self,nums: List[int]) -> int:
        maxval=summ=nums[0]
        for  i in range(1,len(nums)):
            curr=nums[i]   
            if (summ + curr > curr): # if the sum becomes greater than the current value, i am gonna increase it
                summ += curr
            else:  # but if the sum become greater than the current value, the summ becomes the current value
                summ=curr
            maxval=max(maxval,summ)
        return maxval
