class Solution:
    def minOperations(self, s: str) -> int:
        start1 , temp = 0 , s
        for i in range(len(s) - 1):
            if i == 0 and temp[i] == "0":
                start1 += 1
                temp = "1" + temp[1:]
            if temp[i] == temp[i + 1]:
                if temp[i] == "1":
                    temp = temp[:i + 1] + "0" + temp[i + 2 :]
                else:
                    temp = temp[:i + 1] + "1" + temp[i + 2 :]
                start1 += 1
        if not start1:
            return 0
        start0 = 0
        for i in range(len(s) - 1):
            if i == 0 and s[i] == "1":
                start0 += 1
                s = "0" + s[1:]
            if s[i] == s[i + 1]:
                if s[i] == "1":
                    s = s[:i + 1] + "0" + s[i + 2 :]
                else:
                    s = s[:i + 1] + "1" + s[i + 2 :]
                start0 += 1
        return min(start0 , start1)



    