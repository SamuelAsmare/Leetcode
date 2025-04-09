class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if(k>min(nums)):
            return -1
        se=set(nums)
        if(k in se):
            return len(se)-1
        return len(se)
       