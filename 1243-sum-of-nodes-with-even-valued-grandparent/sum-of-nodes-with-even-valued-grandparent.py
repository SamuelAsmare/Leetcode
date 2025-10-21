class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(rooot, parent, grandparent):
            if not rooot:
                return 0
            total = 0
            if grandparent and grandparent % 2 == 0:
                total += rooot.val
            total += dfs(rooot.left, rooot.val, parent)
            total += dfs(rooot.right, rooot.val, parent)
            return total
        return dfs(root, None, None)
