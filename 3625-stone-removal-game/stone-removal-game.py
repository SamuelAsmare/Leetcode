class Solution(object):
    def canAliceWin(self, n):
        takeamount=10
        count=0
        while n>=takeamount:
            n=n-takeamount
            takeamount=takeamount-1
            count=count+1
        return (count%2)!=0
        
        