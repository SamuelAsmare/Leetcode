class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        case1=True
        case2=True
        for i in range(len(word1)):
            if (abs(word1.count(word1[i])-word2.count(word1[i]))  >3):
                case1=False
                break
        for i in range(len(word2)):
            if (abs(word1.count(word2[i])-word2.count(word2[i]))  >3):
                case2=False
                break
        return case1 and case2
