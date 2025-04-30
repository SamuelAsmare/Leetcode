# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(o,p):
            if not o and not p :
                return True
            if (not o or not p):
                return False
            if (o.val != p.val):
                return False
            return check(o.left,p.right) and check(o.right,p.left)
        if not root:
            return True
        return check(root.left,root.right)