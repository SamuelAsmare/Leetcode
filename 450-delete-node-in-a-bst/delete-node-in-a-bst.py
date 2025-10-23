# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_successor(self,node):
        if not node:
            return node
        current = node
        while current.left:
            current = current.left
        return current
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: # if the roor is none return none
            return root
        else:
            if root.val > key:
                root.left = self.deleteNode(root.left , key)
            elif root.val < key:
                root.right = self.deleteNode(root.right , key)
            else:
                if not root.left:
                  return root.right
                elif not root.right:
                    return root.left
                # at this point the root has two children
                temp = self.inorder_successor(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right , root.val)
        return root


        