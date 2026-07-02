# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Get length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Dummy node lets us treat "remove head" like any other removal
        dummy = ListNode(0, head)
        prev = dummy

        # Walk prev to the node just before the one we want to remove
        for _ in range(length - n):
            prev = prev.next

        # Skip over the target node
        prev.next = prev.next.next

        return dummy.next




        