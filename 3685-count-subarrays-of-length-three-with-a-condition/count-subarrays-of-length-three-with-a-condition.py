class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for i in range(n-2):
            if((nums[i]+nums[i+2])*2==nums[i+1]):
                count+=1
        return count