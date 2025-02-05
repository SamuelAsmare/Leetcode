class Solution:
    def reverseBits(self, n: int) -> int:
        samstr=f"{n:032b}"
        samrev=samstr[::-1]
        samint=int(samrev,2)
        return samint
        