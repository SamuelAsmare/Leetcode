# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        elements = []
        def inorder(node):
            nonlocal elements
            if not node:
                return 
            inorder(node.left)
            elements.append(node)
            inorder(node.right)
        inorder(root)
        n = len(elements)
        def construct(start , end):
            if start > end:
                return None
            middle = (start + end)//2
            root = elements[middle]
            root.left = construct(start , middle - 1)
            root.right = construct(middle + 1 , end)
            return root
            
        return construct(0 , n-1)