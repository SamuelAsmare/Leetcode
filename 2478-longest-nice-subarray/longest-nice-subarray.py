class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left, currval, result = 0, 0, 0

        for i in range(len(nums)):
            while (currval & nums[i]) != 0:
                currval ^= nums[left]  
                left += 1
            currval |= nums[i] 
            result = max(result, i - left + 1)

        return result

