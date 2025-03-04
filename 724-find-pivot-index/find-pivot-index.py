class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        rightsum=sum(nums)
        for i in range(len (nums)):
            rightsum-=nums[i]
            if(i>=1):
                 leftsum+=nums[i-1]
            if(rightsum==leftsum):
                return i
        return -1