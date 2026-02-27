class DSU:
    def __init__(self):
        self.parent = {chr(97 + i) : chr(97 + i) for i in range(26)}
    def find(self , x): # with path comprehension
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self , x , y):
        parx = self.find(x)
        pary = self.find(y)
        if parx > pary:
            self.parent[parx] = pary
        else:
            self.parent[pary] = parx
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu , ans = DSU() , ""
        for i in range(len(s1)):
            dsu.union(s1[i] , s2[i])
        for char in baseStr:
            ans = ans + dsu.find(char)
        return ans
