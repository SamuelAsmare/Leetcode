"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Breadth first search
        if not root:
            return
        que = deque([root])
        while que:
            end = que[-1]
            for _ in range(len(que)):
                node = que.popleft()
                if node == end:
                    node.next = None
                else:
                    node.next = que[0]
                if node.right and node.left:
                    que.append(node.left)
                    que.append(node.right)
        return root  
        

                
                

