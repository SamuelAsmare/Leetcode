class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        nums.sort()
        maxval=nums[1]-nums[0]
        for i in range(len(nums)-1):
            curr,nex=nums[i],nums[i+1]
            maxval=max(nex-curr,maxval)
        return maxval
