class Solution:
    def longestPalindrome(self, s: str) -> int:
        fre , flag , ans = Counter(s) , False , 0
        fre = sorted(fre.items(), key=lambda x: x[1])
        if len(fre) == 1:
            return fre[0][1]
        for item in fre:
            if item[1] == 1 and not flag:
                ans += 1
                flag = True
            elif item[1] >= 2 and flag:
                ans += item[1]-item[1]%2
            elif item[1]>=2 and not flag:
                ans += item[1]
                if item[1]%2 !=0:
                    flag=True
        return ans
