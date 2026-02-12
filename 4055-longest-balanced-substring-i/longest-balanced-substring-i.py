class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            fre = defaultdict(int)
            for j in range(i , len(s)):
                prev , balanced = 0 , True
                fre[s[j]] += 1
                for char in fre:
                    if not prev:
                        prev = fre[char]
                    else:
                        if fre[char] != prev:
                            balanced = False
                            break
                if balanced:
                    ans = max(ans , j - i + 1)
        return ans


