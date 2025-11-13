class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [(a^(a>>1)) for a in range(1<<n)]