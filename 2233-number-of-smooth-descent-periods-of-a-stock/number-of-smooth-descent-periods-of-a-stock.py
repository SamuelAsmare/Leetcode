class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans , n , prev = 1 , len(prices) , 1
        for i in range(1,n):
            if prices[i] - prices[i-1] != -1:
                prev = 1
            else:
                prev += 1
            ans += prev
        return ans

        





