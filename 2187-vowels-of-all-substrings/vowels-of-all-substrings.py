class Solution:
    def countVowels(self, word: str) -> int:
        vowels=['a','e','o','i','u']
        count=0
        for i in range (len(word)):
            if (word[i] in vowels):
                count=count+((i+1)*(len(word)-i))
        return count
