class Solution:
    def findKthBit(self , n: int, k: int) -> str:
        if n == 1:return '0'
        middle = 2 ** (n - 1)
        if k == middle:return '1'
        elif k < middle:return self.findKthBit(n - 1, k)
        else:
            bit = self.findKthBit(n - 1, 2 ** n - k)
            return '1' if bit == '0' else '0'

        