class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n,encrypted=len(s),""
        for i in range(n):
            temp=(i+k)%n
            encrypted+=s[temp]
        return encrypted