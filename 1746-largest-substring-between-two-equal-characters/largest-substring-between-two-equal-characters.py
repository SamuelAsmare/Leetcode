class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        maxdistance=0
        hasdouble=False
        for i in range(len(s)):
            temp=s[i]
            s=s[:i]+" "+s[i+1:]
            if(temp in s):
                Index=s.index(temp)
                maxdistance=max(maxdistance,abs(i-Index)-1 )
                hasdouble=True
                s=s[:i]+temp+s[i+1:]
        if(not hasdouble):
                return -1
        else:
            return maxdistance

            
        