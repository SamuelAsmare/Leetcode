class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        rightsum=0
        leftsum=0
        count=0
        for i in range(len(nums)):
            rightsum=rightsum+nums[i]
        for i in range(len(nums)-1):
            leftsum=leftsum+nums[i]
            rightsum=rightsum-nums[i]
            if((leftsum-rightsum)%2==0):
                count=count+1         
        return count
       
        