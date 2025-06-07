class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        losers , n = set() , len(grid)
        for i in range(n):
            for j in range(n):
                if i != j and grid[i][j] == 1:
                    losers.add(j)
        for i in range(n):
            if i not in losers:
                return i
