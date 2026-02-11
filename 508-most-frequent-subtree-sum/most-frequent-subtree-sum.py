# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        fre = defaultdict(int)
        def Sum(node):
            if not node:
                return 0
            curr = node.val
            curr += (Sum(node.left) + Sum(node.right))
            fre[curr] += 1
            return curr
        Sum(root)
        max_fre = max(fre.values())
        ans = []
        for item in fre:
            if fre[item] == max_fre:
                ans.append(item)
        return ans
