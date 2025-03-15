class Solution:
    def sortSentence(self, s: str) -> str:
        splited=s[::-1].split(" ")
        splited.sort()
        for i in range(len(splited)):
            splited[i]= splited[i][::-1]
        s="".join(splited)
        for i in range(len(s)-1):
            if(s[i].isdigit()):
                s=s[:i]+" "+s[i+1:]
        return s[:-1]
