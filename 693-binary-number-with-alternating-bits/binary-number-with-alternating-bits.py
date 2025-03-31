class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binum=bin(n)[2:]
        n=len(binum)
        for i in range(n-1):
            if(binum[i]==binum[i+1]):
                return False
        return True