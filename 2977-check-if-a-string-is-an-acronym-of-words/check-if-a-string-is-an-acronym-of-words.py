class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acronym=True
        if(len(words))!=len(s):
                return False
        for i in range(len(words)):
            
            if(len(s)!=0):
                if(words[i][0] == s[0]):
                     s=s.replace(s[0],"",1)
                else:
                    return False
            else:
                acronym=False
                break
        return acronym