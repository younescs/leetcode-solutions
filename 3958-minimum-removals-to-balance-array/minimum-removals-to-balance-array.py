class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()

        left = 0
        best = 0
        for right in range(len(nums)):
            while nums[right] > nums[left]*k and left < right:
                left +=1
            best = max(best, right - left + 1)

        return len(nums) - best


