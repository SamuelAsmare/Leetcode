class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # the time complexity of log n , and constant space complexity
        if n == 0:
            return False
        prev = 1&n  
        n>>=1 
        while n > 0: # every step right shift the number and check the right most bit
            if not ((prev) ^ (1&n)):
                return False
            prev = 1&n
            n >>= 1
        return True
            


            