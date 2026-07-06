# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result_p, result_q = [], []
        self.inOrderTraversal(p, result_p)
        self.inOrderTraversal(q, result_q)

        print(f"result_p: {result_p}")
        print(f"result_q: {result_q}")
        
        return result_p == result_q
    
    
    def inOrderTraversal(self, node: Optional[TreeNode], result: list) -> list:
        if not node:
            return None
        # if not node.left and not node.right:
        #     result.append(node.val)
        #     return 
        
        self.inOrderTraversal(node.left, result)
        result.append(node.val)
        if not node.right:
            result.append(node.right)
        self.inOrderTraversal(node.right, result)
        