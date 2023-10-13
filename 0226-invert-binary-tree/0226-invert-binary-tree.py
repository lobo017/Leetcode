# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = TreeNode()

        if root == None:
            return None
        
        node = root.right
        root.right = root.left
        root.left = node

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root