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
            arrtuple = tuple(array)
            if arrtuple in dico:
                dico[arrtuple].append(word)
            else:
                dico[arrtuple] = [word]


        return dico.values()