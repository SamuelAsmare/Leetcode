class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indexs, indext = 0 , 0
        while indexs < len(s) and indext < len(t):
            if s[indexs] == t[indext]:
                indexs += 1
            indext += 1
        return indexs == len(s)