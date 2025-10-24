# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def inorder(node , minval , maxval):
            if not node:
                return 
            self.ans = max(self.ans,max(abs(minval - node.val) , abs(maxval - node.val))) 
            inorder(node.left , min(minval,node.val) , max(maxval, node.val))
            inorder(node.right , min(minval,node.val) , max(maxval, node.val))
        inorder(root , root.val , root.val)
        return self.ans