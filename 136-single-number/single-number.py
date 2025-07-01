class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for item in nums:
            ans ^= item
        return ans
