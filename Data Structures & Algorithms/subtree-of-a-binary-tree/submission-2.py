# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue1 = deque([root])
        queue2 = deque([subRoot])
        Subtree_started = False
        
        
        while queue1:
            node1 = queue1.popleft()
            if not node1:
                continue
            if node1.val == subRoot.val:
                Subtree_started = True
                queue1 = deque()
                
            if Subtree_started:
                node2 = queue2.popleft()
                if not node1 and not node2:
                    continue
                
                if not node1 or not node2 or node1.val != node2.val:
                    return False
        
                queue2.append(node2.left)
                queue2.append(node2.right)

            queue1.append(node1.left)
            queue1.append(node1.right)
        
        print(f"queue1: {queue1}")
        print(f"queue2: {queue2}")
                
        return True
        