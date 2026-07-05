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
            return None 
        
        queue = deque([node])
        
        while queue:
            
            n = queue.popleft()
            n.left, n.right = n.right, n.left
            
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
                
        return node
    
    