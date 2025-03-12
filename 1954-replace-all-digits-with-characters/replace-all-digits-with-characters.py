class Solution:
    def replaceDigits(self, s: str) -> str:
        arr=[]
        for i in range(len(s)):
            if (i%2!=0):
                Ascii=ord(s[i-1])
                char=(Ascii + int(s[i]))
                if(char>122):
                    char-=97
                arr.append(chr(char))
            else:
                arr.append(s[i])
            
        return "".join(arr)
            
