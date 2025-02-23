class Solution:
    def consistentcheck(self, s,t)->bool:
        yes=True
        for i in range(len(s)):
            if(s[i] not in t):
                yes= False
                break
        return yes
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter=0
        for i in range(len(words)):
            if(self.consistentcheck(words[i],allowed)):
                counter+=1
        return counter
        