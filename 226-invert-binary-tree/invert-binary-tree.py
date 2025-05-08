# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(root):
            if not root:
                return None
            que = deque([root])
            while que:
                n  = que.popleft()
                n.right , n.left = n.left , n.right
                if (n.left):
                    que.append(n.left)
                if n.right:
                    que.append(n.right)
            return root
        
        return bfs(root)
        