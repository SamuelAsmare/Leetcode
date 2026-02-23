class Solution:
    def longestWord(self, words: List[str]) -> str:
        words_set , ans  = set(words) , ""
        for word in words:
            for i in range(len(word)-1):
                if word[:i+1] not in words_set:
                    break
            else:
                if len(word) > len(ans):
                    ans = word
                elif len(word) == len(ans):
                    ans  =  min(ans , word)
        return ans 

                


