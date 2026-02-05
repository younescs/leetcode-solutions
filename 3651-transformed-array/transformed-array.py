class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        results = [0]*n
        
        for i in range(n):

           results[i] = nums[(i+ nums[i])%n]
            
        return results