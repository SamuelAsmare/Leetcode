class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new=[]
        for i in range(len(s)):
            new.append([s[i],indices[i]])
        new.sort(key=lambda x:x[1])
        s=""
        for i in range(len(new)):
            s=s+str(new[i][0])
        return s