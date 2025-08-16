class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        n = max(len(word) for word in words)
        for i , word in enumerate(words):
            words[i] = words[i].ljust(n)
        vertical =["".join(word).rstrip() for word in zip(*words)]
        return vertical
                
        