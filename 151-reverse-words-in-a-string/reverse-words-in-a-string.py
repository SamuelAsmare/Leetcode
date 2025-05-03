class Solution:
    def reverseWords(self, s: str) -> str:
        splitted=s.split()
        s=splitted[::-1]
        return " ".join(s)
