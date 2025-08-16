class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        n = max(len(word) for word in words)
        result = [] 
        for i in range(len(words)):
            eachrow = words[i]
            
            for j in range(len(words[i]),n):
                eachrow += " "
            words[i] = eachrow
        vertical =["".join(word).rstrip() for word in zip(*words)]
        return vertical
                
        