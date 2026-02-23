class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s) - 1:
            return False
        substrings , right = set() , k-1
        for left in range(len(s) - k + 1):
            substr = s[left : right  + 1]
            substrings.add(substr)
            right += 1
        return len(substrings) == 2**k
# 0 0 1 1 0 1 1 0
# l  