class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if (nums.count(nums[i])%2!=0):
                return False
        return True