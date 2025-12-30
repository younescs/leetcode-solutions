class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        
        nums = [3,2,-1,]
        
        """
    

        
        dico = {0:1}
        counter = 0
        currSum = 0
        for r in nums:
            currSum += r
            diff = currSum - k
            if diff in dico:
                counter += dico[diff]
            dico[currSum] = 1 + dico.get(currSum, 0)
           
        return counter
        

        
    

            