class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        index  , left = 0 , 0
        right = c
        while(right >= left):
            print(left,right)
            if math.isqrt(right)**2 == right:
                return True
            index += 1
            left = index**2
            right = c - left
        return False