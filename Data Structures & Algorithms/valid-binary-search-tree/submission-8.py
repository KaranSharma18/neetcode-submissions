# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.root = root
        return self._isValidBST(root, float("-inf"), float("inf"))
        
    def _isValidBST(self, node: Optional[TreeNode], min_val: int, max_val: int) -> bool:
        if not node:
            return True
        
        if not min_val < node.val < max_val:
            return False
        
        res1 = self._isValidBST(node.left, min_val, node.val)
        res2 = self._isValidBST(node.right, node.val, max_val)

        return res1 and res2

        