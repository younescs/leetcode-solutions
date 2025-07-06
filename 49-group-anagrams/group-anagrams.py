class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dico = {}
        
        for word in strs:
            array = [0]*26
            for letter in word:
                array[ord(letter) - ord("a")] += 1
            array = tuple(array)
            if array in dico:
                dico[array].append(word)
            else:
                dico[array] = [word]


        return dico.values()