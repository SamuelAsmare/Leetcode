class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while(len(s)>2):
            ans=""
            for i in range(len(s)-1):
                ans =ans + str((int(s[i]) + int(s[i+1]))%10 )
            s=ans
        return s[1]==s[0]

        

        