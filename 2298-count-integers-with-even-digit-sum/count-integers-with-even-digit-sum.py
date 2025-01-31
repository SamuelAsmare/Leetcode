class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for i in range(1,num+1,+1):
            if(sum(int(digit) for digit in str(i))%2==0):
                count=count+1
        return count