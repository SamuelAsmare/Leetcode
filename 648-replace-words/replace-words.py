class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words_set = set(dictionary)
        words = sentence.split(" ")
        for i , word in enumerate(words):
            for j in range(len(word)):
                if word[:j+1] in words_set:
                    words[i] = word[:j+1]
                    break
        return " ".join(words)
                    