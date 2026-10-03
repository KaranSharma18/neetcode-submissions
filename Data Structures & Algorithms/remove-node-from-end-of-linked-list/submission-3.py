# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        m = l = 0

        curr = head

        while curr:
            curr = curr.next
            l += 1

        prev, curr = head, head.next

        k = max(0, l - n - 1)

        while curr:
            print("kanxkl")
            if m == k:
                if k == 0:
                    return head.next
                else:
                    prev.next = curr.next

            prev = curr
            curr = curr.next

            m += 1
        
        if m == 0:
            head = None
        
        return head






        