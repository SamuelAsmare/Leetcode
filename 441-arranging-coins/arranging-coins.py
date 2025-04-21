class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans,count=0,1
        while(n>=0):
            n-=count
            count+=1
            ans+=1
        return ans-1
        