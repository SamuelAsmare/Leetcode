class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(x):
            return x == x[::-1]
    
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                cond1  =  s[left+1:right+1] ==   s[left+1:right+1][::-1]
                cond2  =  s[left:right]     ==   s[left:right][::-1]
                return cond1 or cond2
            left += 1
            right -= 1
        return True