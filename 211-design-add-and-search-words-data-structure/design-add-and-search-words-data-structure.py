class Node:
    def __init__(self):
        self.children = dict()
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = Node()
            currNode = currNode.children[char]
        currNode.end = True
        

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.end
               
            if word[index] == ".":
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
                    
            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)
            
            return False
    
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)