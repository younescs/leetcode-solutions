class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list1 = copy.deepcopy(nums)
        list2 = copy.deepcopy(nums)
        output = [0]*len(nums)

   

        for i in range(1, len(nums), 1):
            list1[i] = list1[i-1]* list1[i]
        

        for i in range(len(nums) - 2, -1, -1):
            list2[i] = list2[i]* list2[i+1]

        output[len(nums)- 1] = list1[len(nums)- 2]
        output[0] = list2[1]
        for i in range(1, len(output) - 1, 1):
            output[i] = list1[i-1] * list2[i+1]

        return output