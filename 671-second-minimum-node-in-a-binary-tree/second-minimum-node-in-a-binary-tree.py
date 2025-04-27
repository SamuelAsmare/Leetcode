# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        s=set()
        def b(o):
            if not o:
                return 
            b(o.left) # i am using inorder traversal
            s.add(o.val)
            b(o.right)
        b(root)
        if (len(s)<=1):
            return -1
        val=list(s)
        val.sort()
        return val[1]
