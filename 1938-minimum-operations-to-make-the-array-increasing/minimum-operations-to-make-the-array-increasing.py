class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n,steps=len(nums),0
        for i in range(1,n):
            if(nums[i]<=nums[i-1]):
                steps+=nums[i-1]-nums[i]+1
                nums[i]=nums[i]+nums[i-1]-nums[i]+1
        return steps
