class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 , row2 = set("qwertyuiop") , set("asdfghjkl")
        row3, result = set("zxcvbnm") , []
        for word in words:
            temp = set(word.lower())
            if temp.issubset(row1) or temp.issubset(row2) or temp.issubset(row3):
                result.append(word)
        return result