class Solution:
    def reverseWords(self, s: str) -> str:
        splited=s.split(' ')
        for i in range(len(splited)):
            splited[i]=splited[i][::-1]
        return (" ".join(splited))
