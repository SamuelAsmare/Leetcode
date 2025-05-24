class Solution:
    def findMin(self, nums: List[int]) -> int:
    
        left , right  = 0 , len(nums)-1
        while (right > left):

            mid  =  (left+right)//2

            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid # since it is greater than the right element it cannot be the minimum
            mid = (left+right)//2
        return nums[left]
            

                


