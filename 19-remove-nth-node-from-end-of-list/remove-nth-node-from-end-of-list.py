# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            if n == 1:
                return None
            return head

        dummy = ListNode(None)
        dummy.next = head        
        prev = dummy
        firstp = head
        nxtp = firstp.next
        secondp = head


        for i in range(n):
            secondp = secondp.next


        while secondp:
            nxtp = nxtp.next
            prev = firstp
            firstp = firstp.next
            secondp = secondp.next

        prev.next = nxtp
        firstp.next = None
        

        return dummy.next


