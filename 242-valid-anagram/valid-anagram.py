class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dico = {}

        for i in s:
            if i not in dico:
                dico[i] = 1
            else:
                dico[i] += 1


        for x in t:
            if x not in dico:
                return False
            else:
                if dico[x] == 0:
                    return False
                dico[x] -= 1


        for key in dico:
            if dico[key] != 0:
                return False
        return True