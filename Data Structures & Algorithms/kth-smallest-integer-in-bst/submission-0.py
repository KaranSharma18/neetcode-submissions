# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.inOrderTraversal(root, [])

        return res[k - 1]
    
    def inOrderTraversal(self, node: Optional[TreeNode], res: list) -> list:

        if not node:
            return None
        
        self.inOrderTraversal(node.left, res)
        res.append(node.val)
        self.inOrderTraversal(node.right, res)
        
        return res