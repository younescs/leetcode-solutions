class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        #edge case 1: nums only contains 1 element:
        if len(nums) < 2:
            return False

        #first we're going to create a set to store the array elements in
        aset = set()

        #then we're going to loop through the nums array and store its numbers in the set, if they are aleady in the set, then we return false

        for num in nums:
            if num in aset:
                return True
            aset.add(num)
        return False

        return True