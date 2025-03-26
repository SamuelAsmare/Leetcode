class Solution:
    def findLHS(self, nums: List[int]) -> int:
        left=0
        long=0
        nums.sort()
        for right in range(len(nums)):
            while(nums[right]-nums[left] > 1):
                left+=1
            if(nums[right]-nums[left]==1):
                long=max(long,right-left+1)
        return long