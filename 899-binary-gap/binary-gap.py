class Solution:
    def binaryGap(self, n: int) -> int:
        BIN  , ans , prev = bin(n) , 0 , 0
        for i , item in enumerate(BIN):
            if item == "1":
                if prev:
                    ans = max(ans , i - prev)
                    prev = i
                else:
                    prev = i
        return ans
        

