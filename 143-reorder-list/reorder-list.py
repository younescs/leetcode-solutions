# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        

        fastp = head
        slowp = head

        #finding the middle
        while fastp and fastp.next:
            slowp = slowp.next
            fastp = fastp.next.next

        #reversing the second half:

        prev = None
        curr = slowp

        while curr:
            nxt = curr.next

            curr.next = prev
            prev = curr
            curr = nxt
        
        #re-arranging the linked list:

        
        leftp = head

        rightp = prev

       
        while rightp and rightp.next :

            nxtleft = leftp.next
            leftp.next = rightp

            nxtright = rightp.next
            rightp.next= nxtleft
            
            leftp = nxtleft
            rightp = nxtright



        return head


            