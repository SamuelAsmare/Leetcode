class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 0
        count , counts , ans = 0 , [] , 0
        for i in range(len(s)):
            count += 1
            if i < len(s) - 1 and  s[i] != s[i+1]:
                counts.append(count)
                count = 0
        if(count) != 0:
            counts.append(count)
        for i in range(len(counts)-1):
            ans += min(counts[i] , counts[i+1])
        return ans



