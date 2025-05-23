# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        que  , ans = deque([root]) , []
        while que:
            for _ in range(len(que)):
                temp = que.popleft()
                ans.append(temp.val)
                if temp.right:
                    que.append(temp.right)
                if temp.left:
                    que.append(temp.left)
        return sorted(ans)[k-1]
