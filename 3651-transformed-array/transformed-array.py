class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        
        results = [0]*len(nums)
        
        for i in range(len(nums)):

            if nums[i] == 0:
                results[i] = nums[i]
            if nums[i] > 0:
                index = (i + nums[i]) %len(nums)
                results[i] = nums[index]
            if nums[i] < 0:
                index = i - abs(nums[i])%len(nums)
                results[i] = nums[index]
        
        return results