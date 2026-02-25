class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        self.count = 0
class Solution:
    def __init__(self):
        self.trie = Node()
    def insert(self , word):
        curr = self.trie
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node() 
            curr = curr.children[char]
            curr.count += 1
    def score(self , word):
        ans , curr , terminate = 0 , self.trie , len(word)
        for char in word:
            curr = curr.children[char]
            ans += curr.count
        return ans
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = []
        for word in words:
            self.insert(word)
        for word in words:
            ans.append(self.score(word))
        return ans            

        