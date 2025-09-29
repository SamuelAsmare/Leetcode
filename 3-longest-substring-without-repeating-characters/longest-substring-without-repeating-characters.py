class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right =  0
        longest=0
        for left in range(len(s)):
            while(len(s[left:right+1])==len(set(s[left:right+1])) and right<len(s)):
                longest=max(longest,right-left+1)
                right+=1
        return longest