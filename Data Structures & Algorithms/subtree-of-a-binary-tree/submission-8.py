# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        if root.val == subRoot.val:
            if self._isTreeEqual(root, subRoot):
                return True
                
       
        res1 = self.isSubtree(root.left, subRoot) 
        res2 = self.isSubtree(root.right, subRoot)
        return res1 or res2
    
    def _isTreeEqual(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 and not node2:
            return True
        
        if not node1 or not node2:
            return False
            
        if node1.val == node2.val:
                res1 = self._isTreeEqual(node1.left, node2.left)
                res2 = self._isTreeEqual(node1.right, node2.right)
                return res1 and res2
        
        return False
        