class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        count=0
        stopingindex=len(s)
        for i in range(len(s)):
            if(s[i]==' '):
                count+=1
            if(count>k-1):
                stopingindex=i
                break
        return s[:stopingindex]
            

            
            

        