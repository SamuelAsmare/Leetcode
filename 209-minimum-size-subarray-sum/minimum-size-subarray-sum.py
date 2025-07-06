class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        ans , left , summ = len(nums) , 0 , nums[0]
        if(summ>=target):ans=1
        for right in range(1,len(nums)):
            summ += nums[right]
            while(summ>=target):
                summ -= nums[left]
                ans = min(ans,right-left+1)
                left += 1
        return ans

