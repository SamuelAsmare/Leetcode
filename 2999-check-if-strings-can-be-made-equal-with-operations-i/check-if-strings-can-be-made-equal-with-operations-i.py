class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        s1 = list(s1)
        s2 = list(s2)
        for i in range(2):
            s1[i] , s1[i+2] = s1[i+2] , s1[i]
            if s1 == s2:
                return True
            s1[i] , s1[i+2] = s1[i+2] , s1[i]
        #  swap both
        s1[0] , s1[2] = s1[2] , s1[0]
        s1[1] , s1[3] = s1[3] , s1[1]
        return s1 == s2
