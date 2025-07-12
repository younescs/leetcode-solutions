class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dico = {}

        for i in range(len(numbers)):
            rem = target - numbers[i]
            if rem in dico:
                return [dico[rem], i + 1]
            else:
                dico[numbers[i]] = i + 1

       