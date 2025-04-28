# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        s=set()
        def check(o):
            if not o:
                return True
            check(o.left)
            if (o.val not in s ):
                s.add(o.val)
            check(o.right)
        check(root)
        return len(s)<=1
