class Solution(object):
    def isHappy(self, n):
        newnum=n
        if(n==1):
            return True
        newarr=[]
        while (newnum>=4):
            arr=[int(digits)*int(digits) for digits in str(newnum)]
            newnum=sum(arr)
            if(newnum==1):
                return True
            elif (newnum in newarr):
                return False
            else:
                newarr.append(newnum)
            
        return False
        