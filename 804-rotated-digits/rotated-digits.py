class Solution:
    def rotate(self,num):
        valid , flag = {2 , 5 , 6 , 9 } , False
        invalid  = {3 , 4 , 7}
        while num > 0:
            if num % 10 in invalid:
                return False
            if num % 10 in valid:
                flag = True
            num //= 10
        return flag
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for i in range(1,n+1):
            if self.rotate(i):
                ans += 1
            else:
                print(i)
        return ans


        