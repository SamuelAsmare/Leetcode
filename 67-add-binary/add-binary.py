class Solution:
    def addBinary(self, a: str, b: str) -> str:
        inta=int(a,2)
        intb=int(b,2)
        Sum=inta+intb
        return bin(Sum)[2:]