class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums:
            return min(nums)
        if len(nums) ==1:
            return nums[0]
        left , right  = 0 , len(nums)-1
        minval , flag , =  float("inf") , True
        while (right > left):
            mid  =  (left+right)//2
            
            minval = min(minval,nums[left],nums[right])
           
            if nums[right]>nums[left]:
                right = mid
            else:
                left = mid
            mid =  (left+right)//2
        return minval
            

                


