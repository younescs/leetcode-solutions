class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        # Keep merging until one list is left
        while len(lists) > 1:
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            
            lists = mergedLists
        
        return lists[0]   # final merged list
    
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2
        return dummy.next
