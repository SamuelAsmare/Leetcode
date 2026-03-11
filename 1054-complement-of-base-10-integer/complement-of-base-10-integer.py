class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bits = len(bin(n)) - 2
        mask = (1 << bits) - 1
        return n ^ mask