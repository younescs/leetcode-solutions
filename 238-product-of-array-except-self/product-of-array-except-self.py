class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [0]*len(nums)
        prefix[0] = 1

        for i in range(1, len(nums)):
            prefix[i] = nums[i- 1]* prefix[i - 1]
        
        temp = 1

        for i in range(len(nums)-2, -1, -1):
            temp *= nums[i + 1]
            prefix[i] *= temp
        
        return prefix

    



        