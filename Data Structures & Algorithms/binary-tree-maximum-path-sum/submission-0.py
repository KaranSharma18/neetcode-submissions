# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        self.dfs(root)
        return self.res
    
    def dfs(self, node: Optional[Treenode]) -> int:
        if not node:
            return 0
        
        leftmax = self.dfs(node.left)
        rightmax = self.dfs(node.right)
        leftmax = max(leftmax, 0)
        rightmax = max(rightmax, 0)

        self.res = max(self.res, node.val + leftmax + rightmax)
        return node.val + max(leftmax, rightmax)



        