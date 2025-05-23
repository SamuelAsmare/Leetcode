# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def levelorder(root):
            que , result  = deque([root]) , []
            while que:
                maxval = float("-inf")
                for i in range(len(que)):
                    curr = que.popleft()
                    maxval = max(maxval , curr.val)
                    if curr.left:
                        que.append(curr.left)
                    if curr.right:
                        que.append(curr.right)
                result . append (maxval)
            return result
        return levelorder(root)
