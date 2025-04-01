class Solution:
    def addBinary(self, a: str, b: str) -> str:
        inta,intb=int(a,2),int(b,2)
        Sum=inta+intb
        return bin(Sum)[2:]