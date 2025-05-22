class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        lastindex = 2 
        for i in range(2, n):
            if nums[i] != nums[lastindex - 2]:
                nums[lastindex] = nums[i]
                lastindex += 1
        return lastindex