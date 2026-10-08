class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        #we are first going to create a dictionary which we're going to use to find the set of indices of the solution

        dico = dict()

        #now we're going to go through each one of the element of our list nums and for each element

        for i in range(len(nums)):
            #we're going to calculate the difference between the target sum and the current element
            diff = target - nums[i]

            #if we have that difference stored in our dictionary as a key, then we can simply return the value of that key (which will be the index at which the key, the different in our case, is stored in nums) along side the current index we're looking at in the loop:

            if diff in dico:
                return [dico[diff], i]

            #else, we store the current element we're looking at in nums as a key in our dictionary with the value being the current value of i, the index of the current element we're looking at

            else: 
                dico[nums[i]] = i
            
            