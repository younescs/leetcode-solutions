class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0
        if len(s) < 2:
            return 1

        check = set()
        l = 0
        counter = 0
        check.add(s[l])

        for r in range(1, len(s), 1):
            while s[r] in check:
                check.remove(s[l])
                l += 1
            else:
                check.add(s[r])
                counter = max(counter, len(check))
                    
            
        return counter
        

