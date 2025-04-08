class Solution:
    def reverseDegree(self, s: str) -> int:
        dic={}
        Sum=0
        init=26
        for i in range(97,123):
            dic[chr(i)]=init
            init-=1
        for i,item in enumerate(s):
            Sum+=dic[item]*(i+1)
        return Sum