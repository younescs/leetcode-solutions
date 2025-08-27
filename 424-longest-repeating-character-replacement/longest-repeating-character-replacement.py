class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        aababbba
        """
        l= 0
        counter = 0
        dico = {}
        for r in range(len(s)):
            dico[s[r]] = 1 + dico.get(s[r], 0)
            while (r - l + 1 )- max(dico.values()) > k:
                dico[s[l]] -=1
                l +=1
            counter = max(counter, r - l + 1)
        return counter

            


