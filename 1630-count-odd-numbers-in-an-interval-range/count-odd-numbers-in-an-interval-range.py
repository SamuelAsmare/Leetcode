class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low & 1 and high & 1 :
            return 2 + (high - low - 1)//2
        if low & 1 or high & 1 :
            return 1 + (high - low - 1)//2
        return (high-low)//2
        