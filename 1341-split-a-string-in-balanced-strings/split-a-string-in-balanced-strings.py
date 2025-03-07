class Solution(object):
    def balancedStringSplit(self, s):
        output=0
        R=0
        L=0
        for i in range(len(s)):
            if s[i] == 'R':
                R += 1
            else:
                L += 1
            if(R==L and L>=1 and R>=1):
                output += 1
                R=0
                L=0
        return output

        