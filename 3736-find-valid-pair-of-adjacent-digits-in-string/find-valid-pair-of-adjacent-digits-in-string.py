class Solution:
    def findValidPair(self, s: str) -> str:
        fre,n=Counter(s),len(s)-1
        for i in range (n) :
            curr,nex=int(s[i]),int(s[i+1])
            currfre,nextfre=fre[s[i]],fre[s[i+1]]
            if (curr==currfre and nex==nextfre and curr!=nex):
                return s[i]+s[i+1]
        return ""
