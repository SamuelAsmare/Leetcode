from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while q:  
            if level % 2 == 0:
                prev = float('-inf')
            else:
                prev = float('inf')
            for _ in range(len(q)):
                n = q.popleft()
                if (level % 2 == 0 and (n.val % 2 == 0 or n.val <= prev)) or (level % 2 == 1 and (n.val % 2 == 1 or n.val >= prev)):
                    return False
                prev = n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            level += 1
        return True
