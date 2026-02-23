class Node:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.trie = Node()
    def  insert(self , word):
        curr = self.trie
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.end  = True
    def common(self):
        curr , ans = self.trie , ""
        if len(curr.children) == 0:
            return ans 
        while len(curr.children) == 1 :
            for char in curr.children:
                ans = ans + char
                if curr.children[char].end:
                    return ans
                curr = curr.children[char]
        return ans
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         trie = Trie()
#         for item in strs:
#             if item == "":
#                 return ""
#             trie.insert(item)
#         return trie.common()
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len , ans  = len(strs[0]) , ""
        for item in strs:
            min_len = min(min_len , len(item))
        for i in range(min_len):
            char =  strs[0][i]
            for item in strs:
                if item[i] != char:
                    return ans
            ans += char
        return ans



