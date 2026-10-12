from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        
        prefix = defaultdict(int)
        prefix[0] = 1
        currsum = 0
        result = 0
        for num in nums:
            currsum += num
            diff = currsum - k
            if diff in prefix:
                result += prefix[diff]
            prefix[currsum] += 1
            
        return result