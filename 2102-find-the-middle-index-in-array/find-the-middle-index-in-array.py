class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total , leftsum = sum(nums) , 0
        for i, num in enumerate(nums):
            if leftsum == total - leftsum - num:
                return i
            leftsum += num

        return -1
