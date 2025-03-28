class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxval=max(nums)
        Index=nums.index(maxval)
        for i in range(len (nums)):
            if(maxval==nums[i]):
                continue
            if(nums[i]*2>maxval):
                return -1
        return Index
