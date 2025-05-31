class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = str(grid[i][j])
        ans = [ ]
        cols = [list(column) for column in zip(*grid)]
        for i in range(len(cols)):
            maxlen = 0
            for j in range(len(cols[0])):
                maxlen = max(maxlen,len(cols[i][j]))
            ans.append(maxlen)
        return ans
