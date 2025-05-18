# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def levelorder(root):
            que , result  = deque([root]) , []
            while que:
                right = []
                for i in range(len(que)):
                    curr = que.popleft()
                    right . append(curr.val)
                    if curr.left:
                        que.append(curr.left)
                    if curr.right:
                        que.append(curr.right)
                result . append (right.pop())
            return result 
        return levelorder(root)