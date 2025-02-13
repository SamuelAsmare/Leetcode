class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        size=len(nums)
        proWithNegative=nums[0]*nums[1]*nums[size-1]
        proWithOutNegative=nums[size-1]*nums[size-2]*nums[size-3]
        if(proWithNegative>proWithOutNegative):
            return proWithNegative
        return proWithOutNegative