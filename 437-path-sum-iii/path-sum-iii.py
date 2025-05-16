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
            if not root:
                return
            if (target == root.val):
                result+=1

            path(root.left , target-root.val) 
            path(root.right , target-root.val)
        def paths(root):
            if not root:
                return 
            paths(root.left)
            path(root,targetSum)
            paths(root.right)
        paths(root)
        return result

