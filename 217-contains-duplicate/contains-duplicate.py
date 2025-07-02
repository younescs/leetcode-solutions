class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dico = set()
        
        for i in nums:
            if i in dico:
                return True
            dico.add(i)

        return False
        