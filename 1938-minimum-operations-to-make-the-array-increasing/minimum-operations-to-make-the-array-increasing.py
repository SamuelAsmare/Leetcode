class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n,steps=len(nums),0
        for i in range(1,n):
            prev,curr=nums[i-1],nums[i]
            if(curr<=prev):
                steps+=prev-curr+1
                nums[i]=curr+prev-curr+1
        return steps
