class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Sum=sum(nums[:k])
        maxsum=Sum
        for i in range(k,len(nums)):
            Sum+=nums[i]
            Sum-=nums[i-k]
            maxsum=max(Sum,maxsum)
        return maxsum/k