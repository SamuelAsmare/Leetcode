class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        initialproduct = 1
        while n > 4:
            initialproduct *= 3
            n -= 3
        return initialproduct * n
