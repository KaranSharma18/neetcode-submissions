# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = set()

        while head:
            if head.next in seen:
                return True
            seen.add(head.next)
            head = head.next
        
        return False
        