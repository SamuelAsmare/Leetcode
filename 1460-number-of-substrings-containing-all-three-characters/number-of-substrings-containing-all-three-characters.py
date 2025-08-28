class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = Counter()
        left = 0
        ans = 0
        n = len(s)
        for right, ch in enumerate(s):
            count[ch] += 1
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                ans += n - right  
                count[s[left]] -= 1
                left += 1
        return ans