class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashset = set(nums)
        maxcounter = 0
        for i in range(len(nums)):
            counter = 0
            if (nums[i] - 1) in hashset:
                continue
            else:
                currentNum = nums[i]
                while currentNum in hashset:
                    counter += 1
                    hashset.remove(currentNum)
                    currentNum += 1
            maxcounter = max(maxcounter, counter)


        return maxcounter