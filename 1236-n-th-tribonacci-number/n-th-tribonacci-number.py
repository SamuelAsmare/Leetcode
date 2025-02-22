class Solution:
    def tribonacci(self, n: int) -> int:
        first=0
        second=1
        third=1
        Next=0
        if(n==0):
            return 0
        elif(n==1):
            return 1
        elif(n==2):
           return 1
        elif(n==3):
            return 2
        else:
            for i in range(n-2):
                Next=first+second+third
                first=second
                second=third
                third=Next
        return (Next)
                




        
