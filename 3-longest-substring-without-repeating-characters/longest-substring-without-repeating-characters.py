class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        dico = set()
        l = 0
        counter = 1
        
        if not s:
            return 0
        if len(s) < 2:
            return counter

        dico.add(s[l])
        for r in range(1, len(s), 1):
            if l < r:
                    while s[r] in dico:
                        dico.remove(s[l])
                        l += 1
                    else:
                        dico.add(s[r])
                        counter = max(counter, len(dico))
                    
            
        return counter
        

