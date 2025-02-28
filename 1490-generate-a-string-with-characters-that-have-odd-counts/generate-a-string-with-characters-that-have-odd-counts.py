class Solution:
    def generateTheString(self, n: int) -> str:
        s=""
        if(n%2==0):
            for i in range(n-1):
                s=s+"s"
            s=s+"i"
        else:
            for i in range(n):
                s=s+"s"
        return s
        