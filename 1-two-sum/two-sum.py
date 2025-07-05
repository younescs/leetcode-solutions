class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dico = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in dico:
                return [i, dico[rem]]
            else:
                dico[nums[i]] = i
                



                
        