class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for num in range(low,high+1):
            temp=[int(digits ) for digits in str(num)]
            if(len(temp)%2!=0):
                continue
            mid=len(temp)//2 
            if(sum(temp[:mid])==sum(temp[mid:])):
                count+=1
        return count