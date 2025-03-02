class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left=0
        right=len(s)-1
        while(right>left):
            if (s[left]!=s[right]):
                s=s[:left]+min(s[left],s[right])+s[left+1:]
                s=s[:right]+min(s[left],s[right])+s[right+1:]
            left+=1
            right-=1
        return s