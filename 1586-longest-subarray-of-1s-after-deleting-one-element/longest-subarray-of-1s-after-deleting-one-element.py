class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left , zero , maxval = 0 , 0 , 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero+=1
            while(zero>1):
                if nums[left]==0:
                    zero-=1
                left+=1
            maxval = max(maxval , right - left +1)
        return maxval-1
