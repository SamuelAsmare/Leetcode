class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans , n = 0 , len(prices)
        left = 0
        for right in range(1,n):
            if prices[right] - prices[right-1] != -1:
                subarray_size = right - left
                ans += ((subarray_size*(subarray_size+1))//2)
                left = right
        length = n - left
        ans += length*(length + 1)//2
        return ans
                





