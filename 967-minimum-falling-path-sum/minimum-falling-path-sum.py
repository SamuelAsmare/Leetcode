class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp , n = defaultdict(int) , len(matrix)
        def dfs (row , col):
            if not(0 <= col < n):
                return float("inf")
            if row == n-1:
                dp[(row,col)] = matrix[row][col]
                return dp[(row,col)]
            if (row,col) in dp:
                return dp[(row,col)]
            dp[(row, col)] += matrix[row][col] + min(dfs(row+1 , col-1),dfs(row+1,col) , dfs(row+1,col+1))
            return dp[(row, col)]
        for col , item in enumerate(matrix[0]):
            dfs(0,col)
        print(dp)
        result = float("inf")
        for col , item in enumerate(matrix[0]):
            result = min(result , dp[(0,col)])
        return result
        