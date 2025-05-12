class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet , res = {} , ""
        for i in range(97 , 123):
            alphabet[(i-96)] = chr(i)
        while (s):
            if (s[-1]) == "#":
                res = (alphabet[int(s[-3:-1])]) + res
                s = s[:-3]
            else:
                res = (alphabet[int(s[-1])]) + res
                s = s[:-1]
        return res