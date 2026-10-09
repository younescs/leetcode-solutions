class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        #we are first going to create a dictionary which we're going to use to find the set of indices of the solution

        index_of = dict()

        #now we're going to go through each one of the element of our list nums and for each element

        for i, num in enumerate(nums):
            #we're going to calculate the difference between the target sum and the current element
            diff = target - num

            #if we have that difference stored in our dictionary as a key, then we can simply return the value of that key (which will be the index at which the key, the different in our case, is stored in nums) along side the current index we're looking at in the loop:

            if diff in index_of:
                return [index_of[diff], i]

            #else, we store the current element we're looking at in nums as a key in our dictionary with the value being the current value of i, the index of the current element we're looking at

            else: 
                index_of[num] = i
            
            #now as we loop through nums, we check our dictionary at each step, the dictionary gets progressively filled with the numbers we've seen in nums. if we have the difference between target and the current number we're looking inour dictionary, we've found our solution!