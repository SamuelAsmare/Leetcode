class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x:-(x%2))
        left  , right = 0 , len(nums)-1
        while(left < right):
            nums[right] , nums[left] = nums[left] , nums[right]
            left += 2
            right -= 2
        return nums
       
