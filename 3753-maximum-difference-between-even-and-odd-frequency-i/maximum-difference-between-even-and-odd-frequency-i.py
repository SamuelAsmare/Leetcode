class Solution:
    def maxDifference(self, s: str) -> int:
        fre=Counter(s)
        maxodd=0
        mineven=100
        for i in range(len(s)):
            if((fre[s[i]]%2==0) and (fre[s[i]]<mineven)):
                mineven=fre[s[i]]
            if((fre[s[i]])%2!=0) and (fre[s[i]]>maxodd):
                maxodd=fre[s[i]]
        return maxodd-mineven
        