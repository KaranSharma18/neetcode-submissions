# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        
        result = lists[0]

        for i in range(1, len(lists)):
            result = self.mergeTwoLists(result, lists[i])
        
        return result

    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val >= list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            
            curr = curr.next
        
        curr.next = list1 or list2
        
        return dummy.next





