class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # i am using cyclic sort
        i , ans = 0 , []
        while i < len(nums):
            index = nums[i] -1
            if (nums[i] != nums[index]):
                # swap
                nums[i] , nums[index]  = nums[index] , nums[i]
            else:
                i += 1
        for i , item in enumerate(nums):
            if i+1 != item:
                ans.append(i+1)
        return ans
