class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 :
            return 0

        aset = set(nums)
        anotherset = set()
        
        maxCount = 1

        for i in set(nums):
            if (i-1) in aset:
                continue
            else:
                if (i+1) not in aset: aset.remove(i)
                else: anotherset.add(i)

        for element in anotherset:
            counter = 0
            while element in aset:
                counter +=1
                element +=1
            maxCount = max(counter, maxCount)
    

        return maxCount


      

