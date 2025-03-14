class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        string1=s1.split(' ')
        string2=s2.split(' ')
        
        ans=[]
        for i in range(len(string1)):
            if(string1[i] not in string2 and string1[i] not in ans and string1.count(string1[i])==1):
                ans.append(string1[i])
        for i in range(len(string2) ):
            if (string2[i] not in string1 and string2[i] not in ans and string2.count(string2[i])==1):
                ans.append(string2[i])
        return ans
