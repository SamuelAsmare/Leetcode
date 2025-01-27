class Solution(object):
    def isPowerOfTwo(self, n):
        if(n<0):
            return False
        if(n==0):
            return False
        if(n==1):
            return True
        
        sum=0
        while(n>0):
            sum=sum+(n%2)
            n=n//2
        if(sum==1):
            return True
        else:
            return False
        return False
        