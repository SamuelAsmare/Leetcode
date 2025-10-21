# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ans  = 0
        def inorder(root):
            nonlocal ans
            if root:
                inorder(root.left)
                if root.val % 2 == 0:
                    if root.left and root.left.left:
                        ans += root.left.left.val
                    if root.left and root.left.right:
                        ans += root.left.right.val
                    if root.right and root.right.left:
                        ans += root.right.left.val
                    if root.right and root.right.right:
                        ans += root.right.right.val
                inorder(root.right)
        inorder(root)
        return ans

            
            