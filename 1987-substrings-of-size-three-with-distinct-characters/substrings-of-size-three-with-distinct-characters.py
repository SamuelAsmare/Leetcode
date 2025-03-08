class Solution(object):
    def countGoodSubstrings(self, s):
        count=0
        substr=[s[i:j+1] for i in range(len(s)) for j in range(i+1,len(s)) if ((j-i+1)==3)]
        for i in range(len(substr)):
            if(len(substr[i])==len(set(substr[i]))):
                count+=1
        return count
        