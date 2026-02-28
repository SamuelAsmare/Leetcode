class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD , ans = 10**9+7 , 1
        for i in range(1,n):
            ans = ((ans << (i+1).bit_length()) | i+1)%MOD
        return ans
            
