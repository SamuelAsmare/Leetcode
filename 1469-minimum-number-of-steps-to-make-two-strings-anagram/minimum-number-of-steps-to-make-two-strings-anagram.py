class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter=0
        for i in range(len(t)):
            if(t[i] in s):
                s=s.replace(t[i],"",1)
            else:
                counter+=1
        return counter