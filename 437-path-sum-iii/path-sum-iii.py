# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0
        def path(root,target):
            nonlocal result
            if not root: return   
            if root.val == target: result += 1
            path(root.left , target-root.val)
            path(root.right , target-root.val)

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            path(root,targetSum)
            inorder(root.right)
        inorder(root) # call the traversing function ..
        return result

