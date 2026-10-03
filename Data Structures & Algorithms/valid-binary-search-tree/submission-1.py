# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root)
        
    def _isValidBST(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return None
        
        if node.left:
            if node.left.val >= node.val:
                return False
        
        if node.right:
            if node.val >= node.right.val:
                return False
        
        res1 = self._isValidBST(node.left)
        res2 = self._isValidBST(node.right)

        return res1 and res2

        