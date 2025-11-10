class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # get the common prefix of all numbers , (right shift)
        shifts = 0
        while left < right:
            left  = left >> 1
            right = right >> 1
            shifts += 1
        return left << shifts # can also right >> shifts since 
