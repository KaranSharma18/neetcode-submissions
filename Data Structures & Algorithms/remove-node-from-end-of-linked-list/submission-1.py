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
        print(f"m: {m}, k: {k}")

        while curr:
            print("kanxkl")
            if m == k:
                prev.next = curr.next

            prev = curr
            curr = curr.next

            m += 1
        
        if m == 0:
            head = None
        
        return head






        