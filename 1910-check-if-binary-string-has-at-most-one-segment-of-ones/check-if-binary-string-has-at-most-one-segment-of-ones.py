class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        segment = 0
        for i in range(1,len(s)):
            if s[i] == "1":
                if i - 1 > segment :
                    return False
                segment = i
        return True

# 1 0 0 1
# s = 0

