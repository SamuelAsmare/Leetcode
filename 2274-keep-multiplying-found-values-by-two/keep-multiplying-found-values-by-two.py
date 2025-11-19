class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        elements = set(nums)
        while original in elements:
            original *= 2
        return original
