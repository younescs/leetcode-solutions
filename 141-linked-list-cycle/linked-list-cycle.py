# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return False
        
        curr = head
        curr2 = head.next

        
        while curr2 and curr2.next:
            if curr == curr2:
                return True
            curr = curr.next
            curr2 = curr2.next.next

        return False