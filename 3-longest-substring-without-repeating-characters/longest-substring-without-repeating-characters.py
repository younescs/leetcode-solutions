class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """


        check = set()
        l = 0
        counter = 0

        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l += 1
            else:
                check.add(s[r])
                counter = max(counter, len(check))
                    
            
        return counter
        

