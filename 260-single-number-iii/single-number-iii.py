class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0 
        for num in nums:
            xor ^= num
        diff_bit = xor & -xor  # i am finding the set bit
        a = b = 0
        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]
