class Solution:
    def findValidPair(self, s: str) -> str:
        fre,n=Counter(s),len(s)-1
        for i in range (n) :
            if (fre[s[i]]==int(s[i]) and fre[s[i+1]]==int(s[i+1]) and s[i]!=s[i+1]):
                return s[i]+s[i+1]
        return ""
