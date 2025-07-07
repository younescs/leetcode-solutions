class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dico = {}

        for i in nums:
            if i in dico:
                dico[i] += 1
            else:
                dico[i] = 1

        array = [0]*k
        for i in range(k):
            MaxElement = max(zip(dico.values(), dico.keys()))
            array[i] = MaxElement[1]
            dico.pop(MaxElement[1])

        return array



