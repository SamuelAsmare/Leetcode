class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
    def find(self , x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        parx = self.find(x)
        pary = self.find(y)
        if pary > parx:
            self.parent[pary] = parx
        else:
            self.parent[parx] = pary
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu  , dic = DSU(len(s)) , defaultdict(list)
        for u , v in pairs:
            dsu.union(u, v)
        for i in range(len(s)):
            dic[dsu.find(i)].append(s[i])
        for item in dic:
            dic[item].sort(reverse = True)
        for i in range(len(s)):
            s = s[:i] + dic[dsu.find(i)].pop() + s[i+1:]
        return s        