class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans  , prefix , suffix = [1] * len(nums) , 1 , 1 
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = suffix*ans[i]
            suffix *= nums[i]
        return ans
            