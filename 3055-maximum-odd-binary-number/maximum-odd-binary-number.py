class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        sortit=sorted(s)
        if sortit[0]=='0':
            for i in range(len(sortit)):
                if sortit[i]=='1':
                    sortit[0]='1'
                    sortit[i]='0'
                    break
            return "".join(sortit)[::-1]
        return s


        