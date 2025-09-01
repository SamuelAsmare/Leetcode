class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        roots = set(dictionary)
        for i , word in enumerate(words):
            temp , replaced = "" , False
            for j in range(len(word)):
                temp = word[:j]
                if temp in roots and not replaced:
                    words[i] = temp
                    replaced =True
        return " ".join(words)

