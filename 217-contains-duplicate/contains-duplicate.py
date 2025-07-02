class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dico = set()
        
        for i in range(len(nums)):
            if nums[i] in dico:
                return True
            dico.add(nums[i])

        return False
        