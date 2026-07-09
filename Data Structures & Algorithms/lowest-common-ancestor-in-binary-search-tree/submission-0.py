# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.min_node = min(p.val, q.val)
        self.max_node = max(p.val, q.val)
        
        return self._lowestCommonAncestor(root)
    
    def _lowestCommonAncestor(self, root: Optional[TreeNode]) -> TreeNode:
        
        if not root:
            return None
        
        if self.min_node == root.val or self.max_node == root.val:
            return root
        
        if self.min_node < root.val < self.max_node :
            return root
        
        if self.min_node < root.val and self.max_node < root.val:
            return self._lowestCommonAncestor(root.left)
        else:
            return self._lowestCommonAncestor(root.right)
        