class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxval=0
        minval=10000
        minindex=0
        maxindex=0
        maxres=0
        for i in range(len(prices)):
            if(prices[i]>maxval):
                maxval=prices[i]
                maxindex=i
            if(prices[i]<minval):
                minval=prices[i]
                minindex=i
                maxval=0
            if(minindex<maxindex):
                if(maxval-minval >maxres):
                    maxres=maxval-minval
        return maxres

       

        