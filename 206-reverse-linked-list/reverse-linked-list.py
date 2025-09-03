# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        
        prev = None
        curr = head
        nxt = curr.next

        while curr and curr.next:
            curr.next = prev 
            prev = curr
            curr = nxt
            nxt = nxt.next

        curr.next = prev


        return curr