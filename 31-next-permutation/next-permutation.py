
class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        bp = -1
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                bp = i
        if bp == -1:
            nums.reverse()
            return
        justLargestIdx = -1
        for i in range(bp + 1, n):
            if nums[bp] < nums[i]:
                justLargestIdx = i
        nums[bp], nums[justLargestIdx] = nums[justLargestIdx], nums[bp]
        left , right  = bp + 1 , n - 1
        while left < right:
            nums[right] , nums[left] = nums[left] , nums[right]
            left += 1
            right -= 1
