class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        right=len(nums)-1
        left=0
        maxsum=0
        nums.sort()
        while ( right>left):
            if(nums[left]+nums[right])>maxsum:
                maxsum=nums[left]+nums[right]
            left+=1
            right-=1
        return maxsum