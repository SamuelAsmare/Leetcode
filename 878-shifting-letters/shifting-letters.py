class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix , n = 0 , len(shifts) 
        alphabet = dict()
        for i in range(97,123):
            alphabet[i - 96] = chr(i)
            alphabet[chr(i)] = i-96
        for i in range(n-1,-1,-1):
            prefix += shifts[i]
            shifts[i]=prefix
        for i in range(n):
            asci = alphabet[s[i]] + shifts[i]
            asci = (asci)%26
            if asci==0:
                asci = 26
            s = s[:i] + alphabet[asci] + s[i+1:]
        return s
