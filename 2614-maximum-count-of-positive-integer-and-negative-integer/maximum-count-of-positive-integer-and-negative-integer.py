class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive=0
        negative=0
        for i in range (len(nums)):
            if (nums[i]>0):
                positive+=1
            if(nums[i]<0):
                negative+=1
        return max(positive,negative)