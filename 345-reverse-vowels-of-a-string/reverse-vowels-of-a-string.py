class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u']
        temp=[]
        for i in range(len(s)):
            if (s[i].lower() in vowels):
                temp.append(s[i])
        temp2=temp[::-1]
        string=list(s)
        for i in range(len(string)):
            if(string[i].lower() in vowels):
                string[i]=temp2[0]
                temp2.remove(temp2[0])
        return "".join(string)
                