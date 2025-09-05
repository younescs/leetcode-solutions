# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode(0)

        if list1.val <= list2.val:
            dummy.next = list1
        else:
            dummy.next = list2
           
        curr = list1
        curr2 = list2

        prev = None
        prev2 = None

        
        while curr and curr2:
            if curr.val <= curr2.val:
                while curr and curr.val <= curr2.val:
                    prev = curr
                    curr = curr.next
                prev.next = curr2
            else:
                while curr2 and curr2.val < curr.val:
                    prev2 = curr2
                    curr2 = curr2.next
                prev2.next = curr

        return dummy.next

            
