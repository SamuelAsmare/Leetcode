# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def counter (o):
            if not o:
                return 0
            return 1 + (counter (o.left) + counter (o.right))
        return counter (root)