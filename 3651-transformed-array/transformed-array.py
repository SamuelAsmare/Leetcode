class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result , n = nums.copy() , len(nums)
        for i , item in enumerate(nums):
            if item > 0:
                new_pos = (i + item)%n
                result[i] = nums[new_pos]
            elif item < 0:
                new_pos = (i + item + n)%n
                result[i] = nums[new_pos]
            else:
                result[i] = item
        return result
#  1 - 2 + 4