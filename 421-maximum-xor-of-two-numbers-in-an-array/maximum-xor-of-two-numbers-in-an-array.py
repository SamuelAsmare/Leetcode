class Node:
    def __init__(self):
        self.children = {}
class Solution:
    def __init__(self):
        self.trie = Node()
    def insert(self , word):
        curr = self.trie
        for item in word:
            if item not in curr.children:
                curr.children[item] = Node()
            curr = curr.children[item]
    def max_xor(self , num):
        curr = self.trie
        binary = bin(num)[2:].zfill(32)
        ans = ""
        for char in binary:
            if char == "0":
                opp = "1"
            else:
                opp = "0"
            if opp in curr.children:
                ans = ans + opp
                curr = curr.children[opp]
            else:
                ans = ans + char
                curr = curr.children[char]
        return int(ans , 2 ) ^ num
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            binary = bin(num)[2:].zfill(32)
            self.insert(binary)
        for num in nums:
            ans  = max(ans , self.max_xor(num))
        return ans 