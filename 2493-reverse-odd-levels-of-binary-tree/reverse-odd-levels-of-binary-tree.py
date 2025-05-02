# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def check(left,right,level):
            if not left or not right:
                return 
            if level%2 == 1:
                left.val,right.val=right.val,left.val
            check(left.left,right.right,level+1)
            check(left.right,right.left,level+1)
        check(root.left,root.right,1)
        return root