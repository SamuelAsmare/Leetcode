class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = []
        for i in range(1 , query_row  + 2):
            dp.append([0.00000] * i)
        dp[0][0] = poured
        for i in range(query_row+1):
            for j in range(i+1):
                if dp[i][j] > 1.0000:
                    remainder = dp[i][j] - 1.000
                    dp[i][j] = 1.00
                    if i < query_row:                    
                        dp[i+1][j] += remainder/2.000
                        dp[i+1][j+1] += remainder / 2.00
        return dp[query_row][query_glass]

