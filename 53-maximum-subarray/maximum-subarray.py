class Solution:
    def maxSubArray(self,nums: List[int]) -> int:
        maxval=summ=nums[0]
        for  i in range(1,len(nums)):
            curr=nums[i]
            if (summ + curr > curr):
                summ += curr
            else:
                summ=curr
            maxval=max(maxval,summ)
        return maxval
