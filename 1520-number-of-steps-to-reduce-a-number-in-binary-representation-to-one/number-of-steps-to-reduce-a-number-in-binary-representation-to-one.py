class Solution:
    def add1(self , number):
        for i in range(len(number)-1 , -1 , -1):
            if number[i] == "0":
                number = number[:i] + "1" + number[i+1:]
                break
            else:
                number = number[:i] + "0" + number[i+1:]
        else: 
            number = "1" + number
        return number
    def numSteps(self, s: str) -> int:
        ans = 0
        while len(s) > 1:
            if s[-1] == "1":
                s = self.add1(s)
            else:
                s = s[:-1]
            ans += 1
        return ans
            


        