# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self._invertTree(root)
    def _invertTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return node
        
        if node.left and node.right:
            tmp_node = node.right
            node.right = self._invertTree(node.left)
            node.left = self._invertTree(tmp_node)
            
        elif node.left:
            node.right = self._invertTree(node.left)
            node.left = None
        
        elif node.right:
            node.left = self._invertTree(node.right)
            node.right = None
        
        return node
    
    