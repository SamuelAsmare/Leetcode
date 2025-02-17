class Solution:
    def countElements(self, nums: List[int]) -> int:
       nums.sort()
       counter=0
       for i in range(len(nums)):
        if(nums[i]>nums[0]  and nums[i]<nums[-1]):
            counter+=1
       return counter

        