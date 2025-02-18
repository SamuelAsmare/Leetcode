class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        answer=""
        for i in range(len(t)):
            if(t[i] not in s):
                answer+=t[i]
            else:
                s=s.replace(t[i],"",1)
        return answer

        