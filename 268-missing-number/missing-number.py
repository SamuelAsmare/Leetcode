class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # apply Inverse property of the XOr
        ans = 0
        for i in range(0,len(nums)+1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans 
