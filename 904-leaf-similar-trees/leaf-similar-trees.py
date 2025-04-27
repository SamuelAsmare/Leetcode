# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1,arr2=[],[]
        def c1(o):
            if not o:
                return 
            c1(o.left)
            if (not o.right and not o.left):
                arr1.append(o.val)
            c1(o.right)
        def c2(o):
            if not o:
                return 
            c2(o.left)
            if (not o.right and not o.left):
                arr2.append(o.val)
            c2(o.right)
        c1(root1)
        c2(root2)
        return arr1==arr2
        
