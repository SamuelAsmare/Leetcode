# the question is union find 
class UnionFind: # quick find type
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]
    def find(self , x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x
    def union(self,x,y):
        pary = self.find(y)
        parx = self.find(x)
        if self.rank[parx] > self.rank[pary]:
            self.parent[pary] = parx
        elif self.rank[pary] > self.rank[parx]:
            self.parent[parx] = pary
        else: # if they are equal , lets randomly assign the parent and increase the rank of the parent
            self.parent[parx] = pary
            self.rank[pary] += 1
    def connected(self , x,y):
        return self.find(x) == self.find(y)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = n = len(isConnected) 
        # if they are connected , assign the same parent and decrease the provonce
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j] and uf.find(i) != uf.find(j):
                    uf.union(i,j)
                    province -= 1
        return province


