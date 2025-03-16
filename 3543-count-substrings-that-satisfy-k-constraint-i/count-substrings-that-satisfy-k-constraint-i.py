class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        substr=[s[i:j+1] for i in range(len(s)) for j in range(i,len(s))]
        count=0
        for i in range(len (substr)):
            if(substr[i].count('0')<=k or substr[i].count('1')<=k):
                count+=1
        return count
