class Solution:
    def firstUniqChar(self, s: str) -> int:
        fre=Counter(s)
        for i in range(len(s)):
            if (fre[s[i]]==1):
                return i
        return -1