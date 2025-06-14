class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        maxval = 0

        for right in range(len(nums)):
            if nums[right]==0:
                zeros+=1
            while zeros>1:
                if nums[left]==0:
                    zeros-=1
                left+=1
            print(maxval)
            maxval = max(maxval, right-left+1)
        return maxval-1